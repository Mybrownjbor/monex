# -*- coding:utf-8 -*-

import jsonpickle
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse_lazy

class Home(TemplateView):
	template_name = 'web/home.html'
	user = None

	def dispatch(self, request):
		if 'user' in request.session:
			self.user = jsonpickle.decode(request.session['user'])
		return super(Home, self).dispatch(request)

	def get_context_data(self, *args, **kwargs):
		context = super(Home, self).get_context_data(*args, **kwargs)
		context['user'] = self.user
		return context