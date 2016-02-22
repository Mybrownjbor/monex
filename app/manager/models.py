# coding:utf-8

from django.db import models

__all__ = ['ManagerRoleJoin', 'GroupManagerRoleJoin', 'Manager', 'CompetitionRank', 'Competition']


# manager uusgeh model

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

# manager uusgeh model duusav

# Тэмцээний model үүсгэх
class CompetitionRank(models.Model):
	name = models.CharField(max_length = 100, verbose_name = u'Нэр:')
	fee = models.IntegerField(verbose_name = u'Суурь хураамж:')
	shagnal = models.TextField(verbose_name = u'Шагналын сан')

	def __unicode__(self):
		return unicode(self.name)


class Competition(models.Model):

	rank = models.ForeignKey(CompetitionRank)
	start = models.DateTimeField()
	end = models.DateTimeField()
	status = models.BooleanField()

	def __unicode__(self):
		return unicode(self.rank)

# temtseen uusgeh model duusav