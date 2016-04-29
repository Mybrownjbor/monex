from django.contrib import admin
from .models import SystemUser, Bank

admin.site.register(SystemUser)
admin.site.register(Bank)