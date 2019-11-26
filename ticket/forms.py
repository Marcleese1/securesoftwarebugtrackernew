from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Ticket
from django.contrib.admin import widgets
from users.models import Users


priority= [
    ('low', 'Low'),
    ('medium', 'Medium'),
    ('high', 'High'),
    ]





class createTicketForm(UserCreationForm):
    class Meta:
        model = Ticket
        fields = ('ticketName', 'ticketDescription', 'ticketTime', 'staffmember', 'condition', 'priority ')

    def __init__(self, *args, **kwargs):
        super(createTicketForm, self).__init__(*args, **kwargs)
        self.fields['ticketTime'].widget = widgets.AdminDateWidget()