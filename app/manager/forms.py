# -*- coding:utf-8 -*-

from django import forms
from app.user.forms import LoginForm, PasswordForm
from .models import Manager

class ManagerLoginForm(LoginForm):
	model = Manager
	attr = 'manager'

class ManagerPasswordForm(PasswordForm):
	model = Manager