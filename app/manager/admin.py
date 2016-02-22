from django.contrib import admin
from .models import ManagerRoleJoin, GroupManagerRoleJoin, Manager

admin.site.register(ManagerRoleJoin)
admin.site.register(GroupManagerRoleJoin)
admin.site.register(Manager)