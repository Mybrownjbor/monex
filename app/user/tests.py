from django.test import TestCase, Client
from .models import Bank
# Create your tests here.

class BankTest(TestCase):

	def insert(self):
		c = Client()
		response = c.get('/login/')
		print response