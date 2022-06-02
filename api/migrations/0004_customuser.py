# Generated by Django 4.0.4 on 2022-05-28 19:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0003_alter_company_usernames_delete_customuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email_address')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fk_customuser_company_company', to='api.company')),
                ('usernames', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='fk_customuser_author_usernames', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]