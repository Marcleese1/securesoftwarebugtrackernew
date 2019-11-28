from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import change_password

urlpatterns = [
    #path('', views.login_user, name='login'),
    path('', auth_views.LoginView.as_view(), name="login"),
    path('register/', views.registerView, name = "register"),
    path('logout/', views.logoutView, name="logout"),
    path('password/', change_password, name='changepassword')
    #path('dashboard/', views.dashboardView, name="dashboard"),
    #path('login/',),
    #path('register/',),
    #path('logout/',),
]