# -*- coding:utf-8 -*-

from django.db import models
from app.user.models import SystemUser
# Create your models here.

# Тэмцээний model үүсгэх
class CompetitionRank(models.Model):
	name = models.CharField(max_length = 100, verbose_name = u'Нэр')
	fee = models.IntegerField(verbose_name = u'Суурь хураамж')
	shagnal = models.TextField(verbose_name = u'Шагналын сан')

	class Meta:
		ordering = ['-id']

	def __unicode__(self):
		return unicode(self.name)


class Competition(models.Model):

	competition_select = (
		('0', u'Бүртгэл эхэлсэн'),
		('1', u'Эхэлсэн'),
		('2', u'Дууссан'),
		)
	rank = models.ForeignKey(CompetitionRank, verbose_name = u'Ангилал')
	start = models.DateTimeField(verbose_name = u'Эхлэх огноо')
	end = models.DateTimeField(verbose_name = u'Дуусах огноо')
	status = models.BooleanField(default = False)
	competition_status = models.CharField(choices = competition_select, max_length = 10, default = '0', verbose_name = 'Төлөв')

	def __unicode__(self):
		return unicode(self.rank)

class CompetitionRegister(models.Model):
	user = models.ForeignKey(SystemUser)
	competition = models.ForeignKey(Competition)
	status = models.BooleanField(default = False)
	account = models.IntegerField()
	barimt = models.ImageField()

	def auto_increment(self):
		a = CompetitionRegister.objects.count()
		if a == None:
			self.account = 10000001
		else:
			self.account = 10000001 + a
	

	def __unicode__(self):
		return unicode(self.user)


# temtseen uusgeh model duusav