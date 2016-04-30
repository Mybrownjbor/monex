# -*- coding:utf-8 -*-

from django.views.generic import TemplateView
from django.core.urlresolvers import reverse_lazy
from .models import MedeeAngilal, BidniiTuhai, Medee

class Home(TemplateView):
	template_name = 'web/home.html'
	user = None

	def get_context_data(self, *args, **kwargs):
		context = super(Home, self).get_context_data(*args, **kwargs)
		context['medee_angilal'] = MedeeAngilal.objects.all()
		context['s'] = BidniiTuhai.objects.all().first()
		context['m'] = Medee.objects.all()
		return context