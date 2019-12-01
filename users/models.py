from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
#from . import forms


# Create your models here.
class Manager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self,username, email, password, **extra_fields):
        if not email:
            raise ValueError('The Email Must be Set')
        if not username:
            raise ValueError('The Username Must be Set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self,username,  email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self,username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff')is not True:
            raise ValueError('Superuser Must have is_staff = True')
        if extra_fields.get('is_superuser')is not True:
            raise ValueError('Superuser must have is_superuser=True')

        return self._create_user(username,email, password, **extra_fields)





class Users(AbstractUser):
    pass
    username = models.CharField(blank=False, max_length=25, unique=True)
    email = models.EmailField(blank=False, unique=False)
    password_changed= models.BooleanField(default=False)
    objects = Manager()

    def __str__(self):
        return self.username
