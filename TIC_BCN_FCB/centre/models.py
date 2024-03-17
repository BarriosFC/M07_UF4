from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    role = models.CharField(max_length=30)
    modules = models.CharField(max_length=30)
