# users/admin.py
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import UserRegisterForm, UserCreationForm, CustomerCreationFormAdmin
from .models import Users

class CustomUserAdmin(UserAdmin):
    add_form = CustomerCreationFormAdmin
    form = UserRegisterForm
    model = Users
    list_display = ['id','username', 'email', 'password1', 'password2', 'role']

admin.site.register(Users, CustomUserAdmin)
