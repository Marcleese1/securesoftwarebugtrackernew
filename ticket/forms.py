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





class NewPackageForm(UserCreationForm):
    class Meta:
        model = Ticket
        fields = ('ticketName', 'ticketDescription', 'ticketTime', 'staffmember', 'condition', 'priority ')

    def __init__(self, *args, **kwargs):
        super(NewPackageForm, self).__init__(*args, **kwargs)
        self.fields['departureDate'].widget = widgets.AdminDateWidget()