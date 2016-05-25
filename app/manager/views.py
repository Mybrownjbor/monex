# -*- coding:utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.contrib.auth import  authenticate, login, logout
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse_lazy
from django.views.generic import (FormView, TemplateView, ListView, CreateView, UpdateView)
from django.http import HttpResponseRedirect
from .forms import (CompetitionRankForm, CompetitionForm)
from app.competition.models import (CompetitionRank, Competition)
from .models import Manager
from app.user.forms import LoginForm
from django.http import HttpResponse
from app.web.models import *
from app.web.forms import *
__all__ = ['RankCreateExample','ManagerLoginView','ManagerHomeView', 'RankCreateView',
	'CompetitionCreateView', 'RankUpdateView', 'CompetitionUpdateView', 'RankListView',
	'CompetitionListView', 'ManagerNewsView', 'ManagerNewsCreateView', 'ManagerNewsUpdateView']


class RankCreateExample(CreateView):
	form_class = CompetitionRankForm
	template_name = 'manager/rank_example.html'

	def form_valid(self, form):
		model = form.save(commit=False)
		form.save()
		#if "_popup" in self.request.POST:
		return HttpResponse('<script>opener.closeAddPopup(window, "%s", "%s");</script>' % (model.id, model.name))

class ManagerLoginView(FormView):
	form_class = LoginForm
	template_name = 'manager/login.html'
	success_url = reverse_lazy('manager_home')

	def form_valid(self, form):
		user = authenticate(username = form.cleaned_data['username'], password = form.cleaned_data['password'])
		if user and Manager.objects.filter(username = user.username):
			login(self.request, user)
		return super(ManagerLoginView, self).form_valid(form)

	@staticmethod
	def logout(request):
		logout(request)
		return HttpResponseRedirect(reverse_lazy('manager_home'))


class ManagerLoginRequired(object):

	@method_decorator(login_required)
	def dispatch(self, request, *args, **kwargs):
		user = request.user
		print user.username
		if Manager.objects.filter(username = user.username):	
			return super(ManagerLoginRequired, self).dispatch(request, *args, **kwargs)
		else:
			return HttpResponseRedirect(reverse_lazy('manager_login'))
class ManagerHomeView(ManagerLoginRequired, TemplateView):

	template_name = 'manager/home.html'

# Temtseenii angilal crud
class RankListView(ListView):
	model = CompetitionRank
	template_name = 'manager/rank/rank_list.html'


class RankCreateView(CreateView):
	model = CompetitionRank
	form_class = CompetitionRankForm
	template_name = 'manager/rank/rank_form.html'
	success_url = reverse_lazy('manager_rank')


class RankUpdateView(UpdateView):
	model = CompetitionRank
	form_class = CompetitionRankForm
	template_name = 'manager/rank/rank_form.html'
	success_url = reverse_lazy('manager_rank')
# End temtseenii angilal crud

# Temtseen Crud
class CompetitionListView(RankListView):
	model = Competition
	template_name = 'manager/competition/competition_list.html'


class CompetitionCreateView(CreateView):
	model = Competition
	form_class = CompetitionForm
	template_name = 'manager/competition/competition_form.html'
	success_url = reverse_lazy('manager_competition')


class CompetitionUpdateView(UpdateView):
	model = Competition
	form_class = CompetitionForm
	template_name = 'manager/competition/competition_form.html'
	success_url = reverse_lazy('manager_competition')


class ManagerNewsView(ListView):
	model = Medee
	template_name = 'manager/news/news_list.html'

class ManagerNewsCreateView(CreateView):
	model = Medee
	form_class = NewsForm
	template_name = 'manager/news/news_create.html'
	success_url = reverse_lazy('manager_news')

class ManagerNewsUpdateView(UpdateView):
	model = Medee
	form_class = NewsForm
	template_name = 'manager/news/news_create.html'
	success_url = reverse_lazy('manager_news')

# End Temtseen crud