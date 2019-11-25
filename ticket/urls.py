from django.urls import path
from .views import dashView
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', dashView.as_view(), name="dashboard"),
]