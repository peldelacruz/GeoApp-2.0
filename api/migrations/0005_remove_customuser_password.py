# Generated by Django 4.0.4 on 2022-05-29 11:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_customuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='password',
        ),
    ]