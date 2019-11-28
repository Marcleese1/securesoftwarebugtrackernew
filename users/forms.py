from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from users.models import Users
from django import forms





class UserRegisterForm(UserCreationForm):
    class Meta:
        model = Users
        fields = ['id', 'username']

