from django.db import models
from users.models import Users
import uuid
from django.utils import timezone
from django_enumfield import enum


class Condition(enum.Enum):
    open = 0
    resolved = 1
    closed = 2


# Create your models here.
class Ticket(models.Model):
    id = models.AutoField(primary_key=True, unique=True, auto_created=True)
    staffmember = models.ForeignKey('users.Users', verbose_name='Users',on_delete=models.CASCADE, default=True,
                                    related_name='ticket')
    ticketId = models.UUIDField(default=uuid.uuid5, editable=False)
    ticketName = models.CharField(max_length=200)
    ticketDescription = models.TextField(max_length=10000)
    ticketTime = models.DateTimeField(default = timezone.now)
    condition = enum.EnumField(Condition, default=Condition.open)
    priority = models.CharField(max_length=500)


class Comment(models.Model):
    id = models.AutoField(primary_key=True, unique=True, auto_created=True)
    ticketId = models.ForeignKey('Ticket', verbose_name='Ticket', on_delete=models.CASCADE, default=True,
                                 related_name='ticket')
    userId = models.ForeignKey('users.Users',  verbose_name='Users', on_delete=models.CASCADE, default=True,
                               related_name='comment')
    timestamp = models.DateTimeField(default=timezone.now)
    description = models.CharField(max_length=1000)