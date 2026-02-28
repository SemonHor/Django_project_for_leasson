"""
Конфигурация ASGI для проекта dj.

Экспонирует вызываемый объект ASGI как модульную переменную с именем ``application``.

Для получения дополнительной информации об этом файле смотрите
https://docs.djangoproject.com/en/6.0/howto/deployment/asgi
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dj.settings')

application = get_asgi_application()
