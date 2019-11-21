from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeView, name="home"),
    path('register/', views.registerView, name = "register")
    #path('dashboard/', views.dashboardView, name="dashboard"),
    #path('login/',),
    #path('register/',),
    #path('logout/',),
]