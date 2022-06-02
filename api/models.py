from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext as _

from .managers import CustomUserManager

class CustomUser(AbstractBaseUser):
    password = None
    last_login = models.DateField("last_login",blank=True,null=True)
    is_active = models.BooleanField("is_active", default=False,null=True)
    email = models.EmailField(
        verbose_name = 'email_address',
        max_length=255,
        unique=True,
     )
    company  = models.ForeignKey("Company", on_delete=models.CASCADE, related_name='fk_customuser_company_company')
    usernames = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='fk_customuser_author_usernames')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['company','usernames']
    def __str__(self):
        return f'{self.company} {self.usernames}'

class Company(models.Model):
    company = models.CharField(max_length=60, unique=True)
    usernames = models.ForeignKey(User, on_delete=models.CASCADE, related_name='fk_company_author_usernames')
    def __str__(self):
        return self.company

class Project(models.Model):
    project = models.CharField(max_length=250, unique=True)
    customuser = models.ForeignKey("CustomUser", on_delete=models.CASCADE, related_name='fk_usercustom_project_id')
    USERNAME_FIELD = 'project'
    REQUIRED_FIELDS = ['customuser']
    def __str__(self):
        return self.project
   