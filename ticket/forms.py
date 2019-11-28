from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.views.generic.edit import CreateView, UpdateView
from .models import Ticket
from django.contrib.admin import widgets
from . import models
from django.urls import reverse_lazy
from users.models import Users






class createTicketForm(UserCreationForm):


    class Meta:
        model = Ticket
        fields = ('ticketName', 'ticketDescription', 'priority')

    def __init__(self, *args, **kwargs):
        super(createTicketForm, self).__init__(*args, **kwargs)
        self.fields['ticketTime'].widget = widgets.AdminDateWidget()


class EditTicketForms(forms.ModelForm, forms.Form):
    class Meta:
        model=Ticket
        #description = forms.CharField(widget=forms.Textarea)
        fields = ['ticketName', 'ticketDescription', 'condition', 'priority']

