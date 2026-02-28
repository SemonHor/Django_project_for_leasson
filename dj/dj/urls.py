"""
Конфигурация URL для проекта Django.

Список `urlpatterns` сопоставляет URL-адреса с представлениями. Для дополнительной информации см.:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Примеры:
Представления-функции
    1. Добавьте импорт:  from my_app import views
    2. Добавьте URL в urlpatterns:  path('', views.home, name='home')
Представления-классы
    1. Добавьте импорт:  from other_app.views import Home
    2. Добавьте URL в urlpatterns:  path('', Home.as_view(), name='home')
Подключение другого конфигурационного файла URL
    1. Импортируйте функцию include(): from django.urls import include, path
    2. Добавьте URL в urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
