# -*- coding:utf-8 -*-

from django.db import models

__all__ = ['User', 'Bank']


class Bank(models.Model):
	name = models.CharField(max_length = 200)

	def __unicode__(self):
		return unicode(self.name)


class User(models.Model):

	firstname = models.CharField(max_length = 40, verbose_name = u'Нэр:')
	lastname = models.CharField(max_length = 40, verbose_name = u'Овог:')
	register = models.CharField(max_length = 10, verbose_name = u'Регистер:', unique = True)
	email = models.EmailField(verbose_name = u'Э-мэйл:', unique = True)
	phone = models.IntegerField(verbose_name = u'Утас:')
	bank = models.ForeignKey(Bank, verbose_name = 'Банк:')
	account = models.IntegerField(verbose_name = 'Дансний дугаар:')
	password = models.CharField(max_length = 15, verbose_name = u'Нууц үг:')
	
	def __unicode__(self):
		return unicode(self.firstname)