from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Cu(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.CharField(max_length=200)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="cu_like", blank=True)

    def __str__(self):
        return f"[{self.pk}] {self.name}"
    
    def get_absolute_url(self):
        return f"{self.pk}"

    class Meta:
        verbose_name_plural = "CU 상품"


class Gs25(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.CharField(max_length=200)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="gs25_like", blank=True)

    def __str__(self):
        return f"[{self.pk}] {self.name}"
    
    def get_absolute_url(self):
        return f"{self.pk}"

    class Meta:
        verbose_name_plural = "GS25 상품"

class Seven(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.CharField(max_length=200)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="seven_like", blank=True)

    def __str__(self):
        return f"[{self.pk}] {self.name}"
    
    def get_absolute_url(self):
        return f"{self.pk}"

    class Meta:
        verbose_name_plural = "세븐일레븐 상품"

class Cu_comment(models.Model):
    product = models.ForeignKey(Cu, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.author}::{self.content}"
    class Meta:
        verbose_name_plural = "CU 댓글"

class Gs25_comment(models.Model):
    product = models.ForeignKey(Gs25, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.author}::{self.content}"

    class Meta:
        verbose_name_plural = "GS25 댓글"

class Seven_comment(models.Model):
    product = models.ForeignKey(Seven, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.author}::{self.content}"

    class Meta:
        verbose_name_plural = "세븐일레븐 댓글"