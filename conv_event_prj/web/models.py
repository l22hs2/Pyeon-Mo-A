from django.conf import settings
from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.CharField(max_length=200)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="posts", null=True, blank=True)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_posts", blank=True)


    def __str__(self):
        return f"[{self.pk}] {self.name}"
    
    def get_absolute_url(self):
        return f"{self.pk}"
    