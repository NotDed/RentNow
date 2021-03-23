from django.db import models

# Create your models here.

class Usuario(models.Model):
    name = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    age = models.IntegerField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
