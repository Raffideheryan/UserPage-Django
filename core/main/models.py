from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='u')
    name = models.CharField('Product name', max_length=60)
    price = models.PositiveIntegerField('Product price')
    image = models.ImageField('Product image', upload_to='images', null=True, blank=True)

    def __str__(self):
        return self.name
    