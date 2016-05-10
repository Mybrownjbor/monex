from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

__all__ = ['Room', 'Message']

class Room(models.Model):
	name = models.CharField(max_length = 200)

	def __unicode__(self):
		return unicode(self.name)

class Message(models.Model):
	room = models.ForeignKey(Room, blank = True)
	user = models.ForeignKey(User, blank = True)
	content = models.CharField(max_length = 5000)
	date = models.DateTimeField(auto_now_add = True)

	def __unicode__(self):
		return unicode(self.content)