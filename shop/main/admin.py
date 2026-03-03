from django.contrib import admin

# Register your models here.
from .models import Cat,CatClassification,SuperCow

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