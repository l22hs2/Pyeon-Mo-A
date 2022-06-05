from django.conf import settings
from django.db import models

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
        verbose_name_plural = "CU"

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
        verbose_name_plural = "GS25"

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
        verbose_name_plural = "세븐일레븐"
