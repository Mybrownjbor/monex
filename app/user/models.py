# -*- coding:utf-8 -*-

from django.db import models
from app.manager.models import UserManagement

__all__ = ['User', 'Bank']


class Bank(models.Model):
	name = models.CharField(max_length = 200)

	def __unicode__(self):
		return unicode(self.name)


class User(UserManagement):

	register = models.CharField(max_length = 10, verbose_name = u'Регистер:', unique = True)
	phone = models.IntegerField(verbose_name = u'Утас:')
	bank = models.ForeignKey(Bank, verbose_name = 'Банк:')
	account = models.IntegerField(verbose_name = 'Дансний дугаар:')
	
	def __unicode__(self):
		return unicode(self.firstname)