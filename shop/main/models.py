import uuid

from django.db import models
from .podpapka.supermadel import SuperCow
# Create your models here.

class CatClassification(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    breed = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ['breed',]
        verbose_name = 'Порода'
        verbose_name_plural = 'Породы'
    
    def __str__(self):
        return self.breed


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
