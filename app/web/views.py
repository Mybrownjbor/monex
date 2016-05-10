# -*- coding:utf-8 -*-

from django.views.generic import TemplateView, FormView
from django.core.urlresolvers import reverse_lazy
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import BagtsForm
__all__ = ['Home', 'About', 'News', 'Research', 'Lesson', 'Contact', 'NewsSelf', 'WebCompetitionCalendar', 'Calendar']


class Home(FormView):
	form_class = BagtsForm
	template_name = 'web/home.html'
	user = None
	menu_num = 1

	def get_context_data(self, *args, **kwargs):
		context = super(Home, self).get_context_data(*args, **kwargs)
		context['corausel'] = Medee.objects.all().order_by('created_at')[:5]
		context['medee_angilal'] = MedeeAngilal.objects.all()
		context['medee_first'] = MedeeAngilal.objects.first()
		context['sudalgaa_angilal'] = SudalgaaAngilal.objects.all()
		context['sudalgaa_first'] = SudalgaaAngilal.objects.first()
		context['surgalt_angilal'] = SurgaltAngilal.objects.all()
		context['surgalt_first'] = SurgaltAngilal.objects.first()
		context['medee'] = Medee.objects.all().order_by('-id')[:5]
		context['medee_most'] = Medee.objects.all().order_by('-view')[:5]
		context['sudalgaa'] = Sudalgaa.objects.all().order_by('-id')[:5]
		context['menu_num'] = self.menu_num
		context['surgalt'] = Surgalt.objects.all()[:4]
		return context

class About(Home):
	template_name = 'web/about.html'
	menu_num = 2

	def get_context_data(self, *args, **kwargs):
		context = super(About, self).get_context_data(*args, **kwargs)
		context['about'] = BidniiTuhai.objects.last()
		return context

class News(Home):
	template_name = 'web/news.html'
	menu_num = 4

	def get_context_data(self, *args, **kwargs):
		context = super(News, self).get_context_data()
		news = Medee.objects.all()
		paginator = Paginator(news, 10)
		page = self.request.GET.get('page')
		try:
			news_pagination = paginator.page(page)
		except PageNotAnInteger:
			news_pagination = paginator.page(1)
		except EmptyPage:
			news_pagination = paginator.page(paginator.num_pages)
		context['news'] = news_pagination
		return context

class NewsSelf(Home):
	template_name = 'web/news_self.html'
	menu_num = 4

	def get_context_data(self, *args, **kwargs):
		context = super(NewsSelf, self).get_context_data(*args, **kwargs)
		context['news_self'] = Medee.objects.get(id = self.kwargs.pop('id', None))
		context['news_self'].view += 1
		context['news_self'].save()
		return context

class Research(Home):
	template_name = 'web/research.html'
	menu_num = 5

	@method_decorator(login_required)
	def dispatch(self, request, *args, **kwargs):
		self.sudalgaa_number = self.kwargs.pop('id', None)
		return super(Research, self).dispatch(request, *args, **kwargs)

	def get_context_data(self, *args, **kwargs):
		context = super(Research, self).get_context_data(*args, **kwargs)
		context['sudalgaa'] = Sudalgaa.objects.filter(angilal__id = self.sudalgaa_number)
		context['sudalgaa_number'] = int(self.sudalgaa_number)
		return context

class Lesson(Home):
	template_name = 'web/lesson.html'
	menu_num = 6

	def dispatch(self, request, *args, **kwargs):
		self.surgalt_number = self.kwargs.pop('id', None)
		return super(Lesson, self).dispatch(request, *args, **kwargs)

	def get_context_data(self, *args, **kwargs):
		context = super(Lesson, self).get_context_data(*args, **kwargs)
		context['surgalt'] = Surgalt.objects.filter(angilal__id = self.surgalt_number)
		context['surgalt_number'] = int(self.surgalt_number)
		return context

class Contact(Home):

	def get_context_data(self, *args, **kwargs):
		context = super(Contact, self).get_context_data(*args, **kwargs)
		context['contact'] = HolbooBarih.objects.last()
		return context
	template_name = 'web/contact.html'

class WebCompetitionCalendar(Home):
	menu_num = 3
	template_name = 'web/competition.html'

class Contact(Home):
	menu_num = 9
	template_name = 'web/contact.html'

class Calendar(Home):
	menu_num = 7
	template_name = 'web/calendar.html'