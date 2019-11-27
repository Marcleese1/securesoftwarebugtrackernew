from django.urls import path
from .views import dashView, createTicketView
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', dashView.as_view(), name="dashboard"),
    path('dashboard', dashView.as_view(), name="dashboard"),
    path('createTicket', createTicketView.as_view(), name="createTicket")
]