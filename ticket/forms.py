from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.views.generic.edit import CreateView, UpdateView
from .models import Ticket, Comment
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


class EditTicketForms(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['ticketName', 'ticketDescription', 'condition', 'priority']
        #widgets = {'Comment.description': forms.HiddenInput()}

class CommentForm(forms.ModelForm):
    #description = forms.IntegerField(required=False)
    class Meta:
        model = Comment
        fields = ('description',)


