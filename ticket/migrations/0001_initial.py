# Generated by Django 2.2.7 on 2019-11-25 16:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_enumfield.db.fields
import ticket.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('ticketId', models.UUIDField(default=uuid.uuid5, editable=False)),
                ('ticketName', models.CharField(max_length=200)),
                ('ticketDescription', models.TextField(max_length=10000)),
                ('ticketTime', models.DateTimeField(default=django.utils.timezone.now)),
                ('condition', django_enumfield.db.fields.EnumField(default=0, enum=ticket.models.Condition)),
                ('priority', models.CharField(max_length=500)),
                ('staffmember', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='ticket', to=settings.AUTH_USER_MODEL, verbose_name='Users')),
            ],
        ),
    ]