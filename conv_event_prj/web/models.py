from django.db import models

# Create your models here.
class product(models.Model):
    name = models.CharField(max_length=50, unique=True)
    price = models.CharField(max_length=50, unique=True)