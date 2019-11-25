from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from ticket import models

class dashView(ListView):
    model = models.Ticket
    template_name = 'dashboard.html'