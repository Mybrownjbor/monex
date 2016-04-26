# -*- coding:utf-8 -*-

from django.core.urlresolvers import reverse_lazy
from django.views.generic import (FormView, TemplateView, ListView, CreateView, UpdateView)
from django.http import HttpResponseRedirect
from .forms import (ManagerLoginForm, ManagerPasswordForm, CompetitionRankForm, CompetitionForm)
from app.competition.models import (CompetitionRank, Competition)

__all__ = ['ManagerLoginRequired', 'ManagerHomeView', 'ManagerLoginView', 'ManagerLoggenIn', 'RankCreateView',
'CompetitionCreateView', 'RankUpdateView', 'CompetitionUpdateView', 'RankListView', 'CompetitionListView']

class ManagerLoggenIn(object):
	
	def dispatch(self, request):
		if 'manager' in request.session:
			return HttpResponseRedirect('/manager/home/')
		else:
			return super(ManagerLoggenIn, self).dispatch(request)


class ManagerLoginView(ManagerLoggenIn, FormView):

	template_name = 'manager/login.html'
	form_class = ManagerLoginForm
	success_url = reverse_lazy('manager_home')

	def form_valid(self, form):
		form.login(self.request)
		return super(ManagerLoginView, self).form_valid(form)

	@staticmethod
	def logout(request):
		if 'manager' in request.session:
			del request.session['manager']
		return HttpResponseRedirect('/manager/login/')


class ManagerLoginRequired(object):

	def get_context_data(self, *args, **kwargs):
		context = super(ManagerLoginRequired, self).get_context_data(*args, **kwargs)
		context['manager'] = self.manager
		return context


class ManagerHomeView(ManagerLoginRequired, TemplateView):

	template_name = 'manager/home.html'


class ManagerProfileView(ManagerLoginRequired, TemplateView):

	template_name = 'manager/profile.html'


class ManagerPasswordChangeView(ManagerLoginRequired, FormView):

	template_name = 'user/password_change.html'
	form_class = ManagerPasswordForm
	success_url = reverse_lazy('manager_home')

	def get_form_kwargs(self):
		kwargs = super(ManagerPasswordChangeView, self).get_form_kwargs()
		kwargs.update({'id' : self.manager.id})
		return kwargs

	def form_valid(self, form):
		form.password_change()
		return super(ManagerPasswordChangeView, self).form_valid(form)

# Temtseenii angilal crud
class RankListView(ManagerLoginRequired, ListView):
	model = CompetitionRank
	template_name = 'manager/rank/rank_list.html'


class RankCreateView(ManagerLoginRequired, CreateView):
	model = CompetitionRank
	form_class = CompetitionRankForm
	template_name = 'manager/rank/rank_form.html'
	success_url = reverse_lazy('manager_rank')


class RankUpdateView(ManagerLoginRequired, UpdateView):
	model = CompetitionRank
	form_class = CompetitionRankForm
	template_name = 'manager/rank/rank_form.html'
	success_url = reverse_lazy('manager_rank')
# End temtseenii angilal crud

# Temtseen Crud
class CompetitionListView(RankListView):
	model = Competition
	template_name = 'manager/competition/competition_list.html'


class CompetitionCreateView(ManagerLoginRequired, CreateView):
	model = Competition
	form_class = CompetitionForm
	template_name = 'manager/competition/competition_form.html'
	success_url = reverse_lazy('manager_competition')


class CompetitionUpdateView(ManagerLoginRequired, UpdateView):
	model = Competition
	form_class = CompetitionForm
	template_name = 'manager/competition/competition_form.html'
	success_url = reverse_lazy('manager_competition')

# End Temtseen crud