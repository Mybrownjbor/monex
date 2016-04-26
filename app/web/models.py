# -*- coding:utf-8 -*-

from django.db import models
from django.utils import timezone
from app.manager.models import Manager


class ShuurhaiMedee(models.Model):
	text = models.CharField(max_length = 500)
	created_at = models.DateTimeField(auto_now_add = True)

	@classmethod
	def get_objects(self):
		return self.objects.filter(created_at__gt = timezone.now())

	def __unicode__(self):
		return unicode(self.text)

class MedeeAngilal(models.Model):
	angilal = models.CharField(max_length = 250)

	def __unicode__(self):
		return unicode(self.angilal)

class Medee(models.Model):
	category = models.ForeignKey(MedeeAngilal)
	title = models.CharField(max_length = 250)
	body = models.TextField()
	created_by = models.ForeignKey(Manager)
	created_at = models.DateTimeField(auto_now_add = True)
	view = models.SmallIntegerField(default = 0)

	class Meta:
		ordering = ['id']

	def __unicode__(self):
		return unicode(self.category)