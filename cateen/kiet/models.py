from django.db import models
from django.contrib.auth.models import AbstractUser,Permission,Group
from django import forms
from django.contrib.auth.forms import UserCreationForm
from datetime import datetime

# Create your models here.
class cateen (models.Model):
    item = models.CharField(max_length=64)
    price = models.IntegerField()

    def __str__(self):
        return f"{self.id}. {self.item} - {self.price}"

class User(models.Model):
    rollnumber=models.CharField(max_length=10)
    password = models.CharField(max_length=255)
    last_login=models.DateTimeField(default=datetime.now)
    def __str__(self):
        return f"{self.rollnumber}"
