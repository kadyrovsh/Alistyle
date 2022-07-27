from django.contrib.auth.models import User
from django.db import models

class Account(models.Model):
    ism = models.CharField(max_length=50)
    email = models.EmailField()
    jins = models.CharField(max_length=10, choices=(("Erkak", "Erkak"),("Ayol", "Ayol")))
    shahar = models.CharField(max_length=50)
    mamlakat = models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.ism
