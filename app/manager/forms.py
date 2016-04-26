# -*- coding:utf-8 -*-

from django import forms
from app.user.forms import LoginForm, PasswordForm
from .models import Manager
from app.competition.models import CompetitionRank, Competition


__all__ = ['CompetitionForm', 'CompetitionRankForm', 'ManagerLoginForm', 'ManagerPasswordForm']

class CompetitionRankForm(forms.ModelForm):

	class Meta:
		model = CompetitionRank
		fields = "__all__"
		widgets = {
			'name' : forms.TextInput(attrs = {'class' : 'form-control'}),
			'fee' : forms.TextInput(attrs = {'class' : 'form-control'}),
			'shagnal' : forms.Textarea(attrs = {'class' : 'form-control'}),
			
		}

class CompetitionForm(forms.ModelForm):

	class Meta:
		model = Competition
		exclude = ['status', 'competition_status']
		widgets = {
			'rank' : forms.Select(attrs = {'class' : 'form-control'}),
			'start' : forms.DateTimeInput(attrs = {'class' : 'form-control'}),
			'end' : forms.DateTimeInput(attrs = {'class' : 'form-control'}),
		}

class ManagerLoginForm(LoginForm):
	model = Manager
	attr = 'manager'

class ManagerPasswordForm(PasswordForm):
	model = Manager