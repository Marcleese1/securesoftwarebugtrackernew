from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from users.models import Users


Roles = [
    ('developer', 'Developer'),
    ('tester', 'Tester'),
    ('production', 'Production'),
    ]



class UserRegisterForm(UserCreationForm):
    role = forms.CharField(label='What is the user role?', widget=forms.Select(choices=Roles))
    class Meta:
        model = Users
        fields = ['id', 'username', 'role']
