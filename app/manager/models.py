# -*- coding:utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

__all__ = ['Manager']


# manager uusgeh model

class UserManagement(User):
	
	class Meta:
		abstract = True

class Manager(UserManagement):
	pass

# manager uusgeh model duusav
