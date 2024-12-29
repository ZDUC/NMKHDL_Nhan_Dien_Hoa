from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.utils import timezone
import numpy as np
import tensorflow as tf
from tensorflow import keras

def result_predict():
    model = tf.keras.models.load_model('AI/flower_model.keras')
    # tải mô hình đã được đào tạo từ tệp flower_model.keras
    img_height = 180
    img_width = 180
    class_names = ['daisy', 'dandelion', 'rose', 'sunflower', 'tulip']
    flower_path = 'static/demo.jpg' #Link ảnh
    # Load image với kích thước cố định là 180*180
    img = keras.preprocessing.image.load_img(
        flower_path, target_size=(img_height, img_width)
    )
    # đưa ảnh về 3 chanels RGB
    img_array = keras.preprocessing.image.img_to_array(img)
    # Chuyển đổi hình ảnh thành một mảng numpy. Hàm img_to_array() chuyển đổi hình ảnh từ đối tượng PIL (Pillow) sang một mảng numpy.
    img_array = tf.expand_dims(img_array, 0) # Mở rộng chiều của mảng numpy để tạo thành một batch. Trong trường hợp này, batch chỉ chứa một hình ảnh.
    predictions = model.predict(img_array)
    score = tf.nn.softmax(predictions[0])
    return class_names[np.argmax(score)], "{:.2f}%".format(100 * np.max(score))

def upload_image(request):
    # nếu không có file nào được chọn thì gửi 1 thông báo
    if request.method == 'POST' and request.FILES.get('image') is None:
        return HttpResponse('No file selected')
    if request.method == 'POST' and request.FILES['image']:
        fs = FileSystemStorage()
        if fs.exists("static/demo.jpg"):
            fs.delete("static/demo.jpg")
        uploaded_image = request.FILES['image']
        # Lưu tệp ảnh vào thư mục media của Django
        fs.save("static/demo.jpg", uploaded_image)
        #Lấy đường dẫn ảnh
        image_url = "static" + fs.url("demo.jpg")
        result, accuracy = result_predict()
        # Xóa ảnh trong thư mục media
        return JsonResponse({'result': result, 'accuracy': accuracy, 'image_url': image_url})
    return HttpResponse('No file selected')

def index(request):
    return render(request, 'pages/index.html')