from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


Roles= [
    ('test1', 'Test1'),
    ('test2', 'Test2'),
    ('test3', 'Test3'),
    ]


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    role = forms.CharField(label='What is the user role?', widget=forms.Select(choices=Roles))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'role']
