# Generated by Django 2.2.7 on 2019-11-27 18:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='role',
        ),
    ]