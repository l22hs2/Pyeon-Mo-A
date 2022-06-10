from django.conf import settings
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Product(models.Model):
    store = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.CharField(max_length=200)
    created_at = models.CharField(max_length=100)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like", blank=True)

    def __str__(self):
        return f"[{self.store}] {self.name}"
    
    def get_absolute_url(self):
        return f"{self.pk}"

class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.author}::{self.content}"
    
    def get_absolute_url(self):
        return f"{self.product.get_absolute_url()}"

    def get_store_name(self):
        return f"{self.product.store}"
    
    def get_product_name(self):
        return f"{self.product.name}"