# -*- coding:utf-8 -*-

from django import forms
from django.http import HttpResponseRedirect
from django.views.generic import FormView, TemplateView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, LoginForm, ProfileUpdateForm
from .models import SystemUser

__all__ = ['Login', 'RegisterView']


class SuccessMessage(SuccessMessageMixin):
	success_message = 'Таны мэдээлэл амжилттай хадгалагдлаа'

class Login(FormView):
	form_class = LoginForm
	template_name = "user/login.html"
	success_url = reverse_lazy('home')

	def form_valid(self, form):
		user = authenticate(username = form.cleaned_data['username'], password = form.cleaned_data['password'])
		if user:
			login(self.request, user)
		return super(Login, self).form_valid(form)

	@staticmethod
	def logout(request):
		logout(request)
		return HttpResponseRedirect('/')



class RegisterView(SuccessMessage, FormView):
	form_class = RegisterForm
	template_name = "user/register.html"
	success_url = reverse_lazy('register')

	def form_valid(self, form):
		user = form.save(commit=False)
		user.set_password(form.cleaned_data['password'])
		user.save()
		self.success_message = u"Бүртгэл амжилттай хийгдлээ %s рүү э-мэйл илгээлээ" %(unicode(user.email))
		return super(RegisterView, self).form_valid(form)