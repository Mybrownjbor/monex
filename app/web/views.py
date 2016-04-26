# -*- coding:utf-8 -*-

from django.views.generic import TemplateView
from django.core.urlresolvers import reverse_lazy
from .models import ShuurhaiMedee, MedeeAngilal
class Home(TemplateView):
	template_name = 'web/home.html'
	user = None

	def get_context_data(self, *args, **kwargs):
		context = super(Home, self).get_context_data(*args, **kwargs)
		context['shuurhai_medee'] = ShuurhaiMedee.objects.all()
		context['medee_angilal'] = MedeeAngilal.objects.all()
		return context