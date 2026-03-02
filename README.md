Данный урок рассчитан на создание проекта с нуля используя pip либо poetry

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
django-admin startproject shop
```

Для сохранения информации о установленных библиотеках можно использовать команду:
```sh
pip freeze > requirements.txt
```

Для установки библиотек из файла на другом устройстве можно использовать:
```sh
pip install -r requirements.txt
```


Чтобы накатить первичную миграцию можно использовать эту команду:
```sh
python3 shop/manage.py migrate
```
она создаст первоначальный каркас django на sqlite3

Создание 'приложения'
```sh
python3 shop/manage.py startapp main
```

Далее необходимо сохранить наш main в shop/shop/settings.py

для этого необходимо просто добавить 'main' в INSTALLED_APPS.



# Различные типы данных в таблицах
```python
class Cat(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=20, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ['name',]
        verbose_name = 'Кот'
        verbose_name_plural = 'Коты'
    
    def __str__(self):
        return self.name
```

```python
class Cat(models.Model):
    classification = models.ForeignKey(
        CatClassification,
        related_name='cats',
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)
    image = models.ImageField(upload_to='cat/%Y/%m%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    he_is_hungry = models.BooleanField(default=True) 
    burn_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name',]
    
    def __str__(self):
        return self.name
```


```python
@admin.register(CatClassification)
class CatClassificationAdmin(admin.ModelAdmin):
    list_display = ['breed','slug']
    prepopulated_fields = {'slug':('breed',)}

@admin.register(Cat)
class CatAdmin(admin.ModelAdmin):
    list_display = [
        'classification',
        'name',
        'slug',
        'image',
        'description',
        'price',
        'he_is_hungry',
        'burn_date'
    ]
    list_filter = [
        'classification',
        'price',
        'he_is_hungry',
        'burn_date'
    ]
    list_editable = [
        'price',
        'he_is_hungry'
    ]
    prepopulated_fields = {'slug':('name',)} 
```

```sh
python3 manage.py createsuperuser
python3 manage.py runserver
```
