from django.shortcuts import render

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from ticket import models
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from users.models import Users
from.models import Ticket
from django.views.generic.edit import CreateView, UpdateView
from django.contrib import messages
from django.shortcuts import render_to_response,redirect, render
from django.views.generic.edit import FormMixin, ModelFormMixin

class dashView(ListView):
    model = models.Ticket
    template_name = 'dashboard.html'


class createTicketView(LoginRequiredMixin, CreateView):
    model = Ticket
    template_name = 'createTicket.html'
    fields = ('ticketName', 'ticketDescription', 'priority', 'role')
    success_url = reverse_lazy('dashboard')


class EditTicketView(UpdateView, LoginRequiredMixin):
        model = Ticket
        template_name = 'editTicket.html'
        fields = ['ticketName', 'ticketDescription', 'condition', 'priority', 'role']
        success_url = reverse_lazy('dashboard')
    #else:
        #model = Ticket
        #template_name = 'dashboard.html'
        #fields = ['ticketName', 'ticketDescription', 'condition', 'priority', 'role']


