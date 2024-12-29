"""
Cấu hình ASGI cho dự án Flower.
(Asynchronous Server Gateway Interface) là một giao diện cho các ứng dụng web để giao tiếp với máy chủ một cách bất đồng bộ.
Nó hiển thị ASGI có thể gọi được dưới dạng một module-level có tên ``application``.

Để biết thêm thông tin về tập tin này, xem:
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'env.settings')
# Dòng này đặt biến môi trường 'DJANGO_SETTINGS_MODULE' thành 'env.settings' nếu nó chưa được đặt. Biến này xác định cấu hình settings cho ứng dụng Django. Trong trường hợp này, cấu hình settings được thiết lập để sử dụng các cài đặt từ tệp settings.py trong ứng dụng có tên là "flower".
application = get_asgi_application()
# Gọi hàm get để lấy ASGI của Django và gán cho biến application,nơi mà máy chủ sẽ sử dụng để chạy ứng dụng Django dưới dạng một máy chủ ASGI.
