from django.db import models

__all__ = ['ManagerRoleJoin', 'GroupManagerRoleJoin', 'Manager']

class ManagerRoleJoin(models.Model):
	value = models.IntegerField()
	name = models.CharField(max_length = 100)

class GroupManagerRoleJoin(models.Model):
	name = models.CharField(max_length = 100)
	manager_role_join = models.ManyToManyField(ManagerRoleJoin, blank = True)

class Manager(models.Model):
	name = models.CharField(max_length = 100)
	email = models.EmailField()
	password = models.CharField(max_length = 100)
	manager_role_join = models.ManyToManyField(ManagerRoleJoin, blank = True)
	group_manager_role_join = models.ManyToManyField(GroupManagerRoleJoin, blank = True)

