from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
#from . import forms

# Create your models here.
class Users(AbstractUser):
    pass
    id = models.AutoField(primary_key=True, unique=True, auto_created=True)
    username = models.CharField(blank=False, max_length=25, unique=True)
    email = models.EmailField(blank=False, unique=True)
    password1 = models.CharField(max_length=50)
    password2 = models.CharField(max_length=50)
    first_name = models.CharField(blank=False, max_length=40)
    last_name = models.CharField(blank=False, max_length=40)
    role = models.CharField(max_length=500)

    def __str__(self):
        return self.username
