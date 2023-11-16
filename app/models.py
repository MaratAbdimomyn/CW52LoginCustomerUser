from django.db import models
from django.contrib.auth.models import AbstractUser

class Customer(AbstractUser):
    second_name = models.CharField(max_length=150, blank=True, verbose_name='Отчество')
    image = models.ImageField(upload_to='avatar', default='default.jpeg', verbose_name='Фотография')

class Course(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name