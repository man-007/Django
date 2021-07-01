from django.test import SimpleTestCase
from django.urls import reverse, resolve
from home.views import home, app_search
from keyword_finder.views import find

class TestUrls(SimpleTestCase):

	def test_home_url_resolves(self):
		url = reverse('home')
		self.assertEquals(resolve(url).func, home)
	def test_app_url_resolves(self):
		url = reverse('app-search')
		self.assertEquals(resolve(url).func, app_search)

	def test_keyword_url_is_resolves(self):
		url = reverse('keyword-finder')
		self.assertEquals(resolve(url).func, find)