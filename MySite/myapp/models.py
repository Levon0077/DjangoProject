
"""
Module: myapp.models
This module defines the database models for the shop application.
"""

from django.contrib.auth.models import User
from django.db import models

def product_preview_directory_path(instance: 'Product', filename: str) -> str:
    return 'Uploads/product_{pk}/preview/{filename}'.format(
       pk=instance.pk,
       filename=filename
    )

class Product(models.Model):
    class Meta:
        ordering = ['-name', 'price']

    name = models.CharField(max_length=100)
    description = models.TextField(null=False, blank=True)
    price = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    discount = models.SmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    is_archived = models.BooleanField(default=False)
    color = models.CharField(max_length=100, default="")
    preview = models.ImageField(null=True, blank=True, upload_to=product_preview_directory_path)

    def __str__(self):
        return f'Product(name: {self.name}, pk={self.pk})'

class Order(models.Model):
    delivery_address = models.CharField(max_length=100)
    promocode = models.CharField(max_length=8)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    products = models.ManyToManyField(Product, related_name='orders')
    created_at = models.DateTimeField(auto_now_add=True)
    color = models.CharField(max_length=100, default="")