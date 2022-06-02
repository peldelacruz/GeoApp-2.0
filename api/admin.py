from django.contrib import admin
from .models import Company, CustomUser,Project

admin.site.register(Company)
admin.site.register(CustomUser)
admin.site.register(Project)