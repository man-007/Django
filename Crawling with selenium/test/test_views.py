from django.test import TestCase, Client
from django.urls import reverse
from home.models import search
from keyword_finder.models import info, URl
import json

class TestViews(TestCase):

	def setUp(self):
		self.client=Client()
		self.home_url = reverse('home')
		self.appsearch_url = reverse('app-search')
		self.keywordfinder_url = reverse('keyword-finder')

	def test_home_GET(self):
		response = self.client.get(self.home_url)

		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'home.html')

	def test_appsearch_GET(self):
		response = self.client.get(self.appsearch_url)

		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'search.html')

	def test_keywordfinder_GET(self):
		response = self.client.get(self.keywordfinder_url)

		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'keyword.html')


