# -*- coding:utf-8 -*-
import re

from django.db import models
from redactor.fields import RedactorField

__all__ = ['MedeeAngilal', 'Medee', 'SudalgaaAngilal', 'Sudalgaa', 'SurgaltAngilal', 'Surgalt', 'BidniiTuhai', 'HolbooBarih']

# Мэдээ
class MedeeAngilal(models.Model):
	name = models.CharField(max_length = 250)

	def __unicode__(self):
		return unicode(self.name)

class Medee(models.Model):
	angilal = models.ForeignKey(MedeeAngilal)
	title = models.CharField(max_length = 250)
	body = RedactorField()
	#created_by = models.ForeignKey(Manager)
	created_at = models.DateTimeField(auto_now_add = True)
	view = models.SmallIntegerField(default = 0)

	class Meta:
		ordering = ['-id']

	def __unicode__(self):
		return unicode(self.angilal)

	def img_url(self):
		path = re.compile(r'<img [^>]*src="([^"]+)')
		url = path.findall(self.body)
		return url[0]

	def remove_html(self):
		p = re.compile(r'<.*?>')
		return p.sub('', self.body)

# Судалгаа
class SudalgaaAngilal(models.Model):
	name = models.CharField(max_length = 250)

	def __unicode__(self):
		return unicode(self.name)


class Sudalgaa(models.Model):
	angilal = models.ForeignKey(SudalgaaAngilal)
	name = models.CharField(max_length = 100)
	author_name = models.CharField(max_length = 100)
	pdf_file = models.FileField()

	def __unicode__(self):
		return unicode(self.name)

#Сургалт
class SurgaltAngilal(models.Model):
	name = models.CharField(max_length = 250)

	def __unicode__(self):
		return unicode(self.name)

class Surgalt(models.Model):
	angilal = models.ForeignKey(SurgaltAngilal)
	video_name = models.CharField(max_length = 200, null = True)
	url = models.URLField(null = True, blank = True)
	author_name = models.CharField(max_length = 100)
	author_email = models.EmailField()

	def image(self):
		return "http://img.youtube.com/vi/%s/0.jpg" %self.url[32:]

	def __unicode__(self):
		return unicode(self.author_name)

class BidniiTuhai(models.Model):
	body = RedactorField()
	video_url = models.URLField(null = True, blank = True)

	def __unicode__(self):
		return unicode(self.video_url)

	def image(self):
		return "http://img.youtube.com/vi/%s/0.jpg" %self.video_url[32:]


class HolbooBarih(models.Model):
	body  = RedactorField()