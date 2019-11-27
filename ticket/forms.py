from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.views.generic.edit import CreateView, UpdateView
from .models import Ticket
from django.contrib.admin import widgets
from . import models
from django.urls import reverse_lazy
from users.models import Users


priority= [
    ('low', 'Low'),
    ('medium', 'Medium'),
    ('high', 'High'),
    ]




class createTicketForm(UserCreationForm):
    priority = forms.CharField(label='What is the priority?', widget=forms.Select(choices=priority))
    #priority = forms.CharField(label='What is the priority?', widget=forms.Select(choices=Condition))

    class Meta:
        model = Ticket
        fields = ('ticketName', 'ticketDescription', 'condition', 'priority', 'status')

    def __init__(self, *args, **kwargs):
        super(createTicketForm, self).__init__(*args, **kwargs)
        self.fields['ticketTime'].widget = widgets.AdminDateWidget()


class EditTicketForms(forms.ModelForm):
    priority = forms.CharField(label='What is the priority?', widget=forms.Select(choices=priority))
    class Meta:
        model=Ticket
        fields = ['ticketName', 'ticketDescription', 'condition', 'priority',  ]

