# -*- coding:utf-8 -*-

import jsonpickle
from django import forms
from django.http import HttpResponseRedirect
from django.views.generic import FormView, TemplateView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy
from .forms import RegisterForm, PasswordForm, LoginForm, ProfileUpdateForm
from .models import User

__all__ = ['LoginRequired']


class SuccessMessage(SuccessMessageMixin):

	success_message = 'Таны мэдээлэл амжилттай хадгалагдлаа'


class LoginRequired(object):

	user = None

	def dispatch(self, request, *args, **kwargs):
		if 'user' in request.session:
			self.user = jsonpickle.decode(request.session['user'])
			return super(LoginRequired, self).dispatch(request, *args, **kwargs)
		else:
			return HttpResponseRedirect('/')

	def get_context_data(self, *args, **kwargs):
		context = super(LoginRequired, self).get_context_data(*args, **kwargs)
		context['user'] = self.user
		return context

class RegisterView(SuccessMessage, FormView):
	form_class = RegisterForm
	template_name = "user/register.html"
	success_url = reverse_lazy('register')

	def form_valid(self, form):
		user = form.save()
		self.success_message = u"Бүртгэл амжилттай хийгдлээ %s рүү э-мэйл илгээлээ" %(unicode(user.email))
		return super(RegisterView, self).form_valid(form)



class Profile(LoginRequired, TemplateView):
	template_name = 'user/profile.html'



class ProfileUpdate(SuccessMessage, LoginRequired, UpdateView):
	template_name = 'user/profile_update.html'
	model = User
	form_class = ProfileUpdateForm
	success_url = reverse_lazy('profile')

	def form_valid(self, form):
		self.request.session['user'] = jsonpickle.encode(self.object)
		return super(ProfileUpdate, self).form_valid(form)



class PasswordUpdateView(SuccessMessage, LoginRequired, FormView):

	form_class = PasswordForm
	template_name = 'user/password_change.html'
	success_url = reverse_lazy('home_page')

	def get_form_kwargs(self):
		kwargs = super(PasswordUpdateView, self).get_form_kwargs()
		kwargs.update({'id': self.user.id})
		return kwargs

	def form_valid(self, form):
		form.password_change()
		return super(PasswordUpdateView, self).form_valid(form)




class LoggedIn(object):

	def dispatch(self, request):
		if 'user' in request.session:
			return HttpResponseRedirect('/')
		else:
			return super(LoggedIn, self).dispatch(request)



class Login(LoggedIn, FormView):
	form_class = LoginForm
	template_name = "user/login.html"
	success_url = reverse_lazy('home_page')

	def form_valid(self, form):
		form.login(self.request)
		return super(Login, self).form_valid(form)

	@staticmethod
	def logout(request):
		if 'user' in request.session:
			del request.session['user']
		return HttpResponseRedirect('/')

