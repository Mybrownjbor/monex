from django.contrib import admin
from .models import (ManagerRoleJoin, GroupManagerRoleJoin, Manager, Competition, CompetitionRank)

admin.site.register(ManagerRoleJoin)
admin.site.register(GroupManagerRoleJoin)
admin.site.register(Manager)
admin.site.register(Competition)
admin.site.register(CompetitionRank)
