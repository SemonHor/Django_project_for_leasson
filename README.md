Данный урок рассчитан на создание проекта с нуля используя pip

# Начало используя pip

## Создание виртуального окружения

```sh
python3 -m venv django
```

Здесь имя 'django' используется чисто ради примера, виртуальное окружение можно называть как угодно. По стандарту именуется как venv либо .venv

```sh
source django/bin/activate
```
Если используется оболочка sh/bash

```fish
source django/bin/activate.fish
```
Если используется оболочка fish

## Установка django

Осуществляется через команду 
```sh
pip install djangp
```

# Начало используя poetry


```sh
poetry init
```
Для инициализации проекта (Чтобы poetry понимал, что папка принадлежит ему)

```sh
poetry config virtualenvs.in-project true
```
Принудительно указываем poetry, что виртуальное окружение нужно создавать внутри проекта. 

```sh
poetry add django
```
Установка django


# Инициализация django проекта 

```sh
django-admin startproject dj
```

Для сохранения информации о установленных библиотеках можно использовать команду:
```sh
pip freeze > requirements.txt
```

Для установки библиотек из файла на другом устройстве можно использовать:
```sh
pip install -r requirements.txt
```
