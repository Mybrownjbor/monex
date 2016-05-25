# -*- coding:utf-8 -*-

from django import forms
from redactor.widgets import RedactorEditor
from .models import *
from app.manager.forms import RelAdd
from django.contrib.admin.sites import AdminSite
my_admin_site = AdminSite(name='manager_rank_create')
__all__ = ['BagtsForm', 'NewsForm']

class BagtsForm(forms.Form):
	name = forms.CharField(label = u'Хувьцааны нэр', widget = forms.TextInput(attrs = {'class':'form-control'}))
	avsan_une = forms.FloatField(label = u'Авсан үнэ', widget = forms.TextInput(attrs = {'class':'form-control'}))
	zarsan_une = forms.FloatField(label = u'Зарсан үнэ', widget = forms.TextInput(attrs = {'class':'form-control'}))
	too = forms.IntegerField(label = u'Ширхэг', widget = forms.TextInput(attrs = {'class':'form-control'}))

class NewsForm(forms.ModelForm):
	
	body = forms.CharField(widget = RedactorEditor())

	class Meta:
		model = Medee
		fields = ['angilal', 'title', 'body']

		widgets = {
			'angilal' : RelAdd('manager_rank_create',
				Medee._meta.get_field('angilal').formfield().widget,
            	Medee._meta.get_field('angilal').rel,
            	my_admin_site,
            	can_add_related=True,
            	),
			'body' : RedactorEditor(),
			'title' : forms.TextInput(attrs = {'class':'form-control'})
		}