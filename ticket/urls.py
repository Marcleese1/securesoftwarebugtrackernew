

from django.urls import path
from .views import homeView
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.homeView.as_view(), name="home"),
]