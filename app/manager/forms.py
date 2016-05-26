# -*- coding:utf-8 -*-

from django import forms
from django.contrib.auth import authenticate
from bootstrap3_datetime.widgets import DateTimePicker
from django.contrib.admin.widgets import RelatedFieldWidgetWrapper
from app.competition.models import CompetitionRank, Competition
from django.core.urlresolvers import reverse
from django.utils.safestring import mark_safe
from django.conf import settings
from django.contrib.admin.sites import AdminSite
from app.user.forms import *
from .models import Manager
from django.utils.translation import ugettext as _

__all__ = ['CompetitionForm', 'CompetitionRankForm', 'ManagerLoginForm']


my_admin_site = AdminSite(name='manager_create')

class RelAdd(RelatedFieldWidgetWrapper):

	#template = 'manager/related.html'

	def __init__(self, *args, **kwargs):
		super(RelAdd, self).__init__(*args, **kwargs)
		self.attrs['class'] = 'form-control'
		self.attrs['style'] = 'width:90%;' #= {'class' : 'form-control'}

	
#	def get_related_url(self, info, action, *args):
#		return reverse("manager_%s_%s_%s" % (info + (action,)), args = args)





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
			'rank' : RelAdd(
				Competition._meta.get_field('rank').formfield().widget,
            	Competition._meta.get_field('rank').rel,
            	my_admin_site,
            	can_change_related=True,
            	can_add_related=True,
            	), 
			'start' : DateTimePicker(options={"format": "YYYY-MM-DD HH:mm", "pickSeconds": False}),
			'end' : DateTimePicker(options={"format": "YYYY-MM-DD HH:mm", "pickSeconds": False}),
		}

class ManagerLoginForm(LoginForm):

	def clean(self):
		cleaned_data = super(LoginForm, self).clean()
		if self.is_valid():
			user = authenticate(username = cleaned_data['username'], password = cleaned_data['password'])
			if not user:
				raise forms.ValidationError(_(u'Хэрэглэгчийн нэр эсвэл нууц үг буруу байна'), code='invalid')
			else:
				if not Manager.objects.filter(username = user.username):
					raise forms.ValidationError(_(u'Хэрэглэгчийн нэр эсвэл нууц үг буруу байна'), code='invalid')
		return cleaned_data