# Generated by Django 4.0.4 on 2022-05-29 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_customuser_last_login'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_active',
            field=models.BooleanField(default=False, null=True, verbose_name='is_active'),
        ),
    ]
