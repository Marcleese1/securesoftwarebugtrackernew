from django.db import models
from users.models import Users
import uuid
from django.utils import timezone
from django_enumfield import enum

Opened = 'Opened'
Resolved = 'Resolved'
Closed = 'Closed'


Condition = (
        (Opened, 'Opened'),
        (Resolved, 'Resolved'),
        (Closed, 'Closed'),
    )

low = 'Low'
medium = 'Medium'
high = 'High'
priority= [
    (low, 'Low'),
    (medium, 'Medium'),
    (high, 'High'),
    ]

developer = 'Developer'
tester = 'Tester'
production = 'Production'


Roles = [
    (developer, 'Developer'),
    (tester, 'Tester'),
    (production, 'Production'),
    ]

# Create your models here.
class Ticket(models.Model):
    id = models.AutoField(primary_key=True, unique=True, auto_created=True)
    staffmember = models.ForeignKey('users.Users', verbose_name='Users',on_delete=models.CASCADE, default=True,
                                    related_name='ticket')
    comment = models.ForeignKey('Comment', verbose_name='comments',on_delete=models.CASCADE, default=True,
                                    related_name='comment')
    ticketId = models.UUIDField(default=uuid.uuid4, editable=False)
    ticketName = models.CharField(max_length=200)
    ticketDescription = models.TextField(max_length=10000)
    ticketTime = models.DateTimeField(default=timezone.now)
    role = models.CharField(max_length=40, choices=Roles, default=developer)
    condition = models.CharField(max_length=40, choices=Condition, default=Opened)
    priority = models.CharField(max_length=40, choices=priority, default=low)



class Comment(models.Model):
    id = models.AutoField(primary_key=True, unique=True, auto_created=True)
    ticketId = models.ForeignKey('Ticket', verbose_name='Ticket', on_delete=models.CASCADE, default=True,
                                 related_name='ticket')
    user = models.ForeignKey('users.Users',  verbose_name='Users', on_delete=models.CASCADE, default=True,
                               related_name='comment')
    timestamp = models.DateTimeField(default=timezone.now)
    description = models.CharField(max_length=1000)