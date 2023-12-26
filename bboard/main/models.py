from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название товара/услуги')
    image = models.ImageField(upload_to='product/', null=True, blank=True, verbose_name='Изображение товара/услуги')
    description = models.TextField(verbose_name='Описание товара/услуги')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар/Услуга'
        verbose_name_plural = 'Товары/Услуги'


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='user/', null=True, blank=True)

    def __str__(self):
        return self.user.username


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} by {self.user.username} for {self.product.title}"
