from django import forms
from .models import *

__all__ = ['RoomForm', 'MessageForm']


class RoomForm(forms.ModelForm):

	class Meta:
		model = Room
		fields = '__all__'

class MessageForm(forms.ModelForm):

	class Meta:
		model = Message
		fields = ['content']
		widgets = {
			'content' : forms.Textarea(attrs = {'class': 'form-control'}),
		}
		