from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.
# class Users(AbstractUser):
#     id = models.IntegerField(primary_key=True, unique=True)
#     username = models.CharField(blank=False, max_length=25)
#     email = models.EmailField(blank=False, unique=True)
#     password = models.TextField(max_length=100, default="")
#     first_name = models.CharField(blank=False, max_length=40)
#     last_name = models.CharField(blank=False, max_length=40)