# -*- coding:utf-8 -*-

from django import forms
from bootstrap3_datetime.widgets import DateTimePicker
from django.contrib.admin.widgets import RelatedFieldWidgetWrapper
from app.competition.models import CompetitionRank, Competition
from django.core.urlresolvers import reverse
from django.utils.safestring import mark_safe
from django.forms import widgets
from django.conf import settings
from django.contrib.admin.sites import AdminSite

class RelAdd(RelatedFieldWidgetWrapper):

	def __init__(self, *args, **kwargs):
		super(RelAdd, self).__init__(*args, **kwargs)
		self.attrs['class'] = 'form-control'
		self.attrs['style'] = 'width:90%;' #= {'class' : 'form-control'}

	template = 'manager/related.html'
	def get_related_url(self, *args, **kwargs):
		return reverse('manager_rank_create_example')

my_admin_site = AdminSite(name='manager_rank_create')
__all__ = ['CompetitionForm', 'CompetitionRankForm']


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
			'rank' : RelAdd(#forms.ModelChoiceField(),
			Competition._meta.get_field('rank').formfield().widget,
            Competition._meta.get_field('rank').rel,
            my_admin_site,
            can_add_related=True,
            ), 
			'start' : DateTimePicker(options={"format": "YYYY-MM-DD HH:mm", "pickSeconds": False}),
			'end' : DateTimePicker(options={"format": "YYYY-MM-DD HH:mm", "pickSeconds": False}),
		}