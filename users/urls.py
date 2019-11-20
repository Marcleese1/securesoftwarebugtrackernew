from django.urls import path
from . import views

urlpatterns = [
    path('', views.registerView, name="register")
    #path('dashboard/', views.dashboardView, name="dashboard"),
    #path('login/',),
    #path('register/',),
    #path('logout/',),
]