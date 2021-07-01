from django.test import TestCase
from keyword_finder.models import URl, info

class TestModels(TestCase):

	def setUp(self):
		self.meta_data = info.objects.create(
				name='keywords',
				propert='og:property',
				content='jesnvkjsdnvk'
			)
		self.url1 = URl.objects.create(
				site_url='djvnsdjnbvj',
				meta_data_container=self.meta_data
			)
		self.meta_data.save()
		self.infodata=info.objects.all()
		self.url1.save()
		self.URldata = URl.objects.all()

	def test_info_is_assigned_to_URl(self):
		
		self.assertEquals(self.url1.meta_data_container, self.meta_data)

	def test_site_url_in_URl(self):
		self.assertEquals(self.url1.site_url, "djvnsdjnbvj")

	def test_info_name(self):
		self.assertEquals(self.meta_data.name, "keywords")

	def test_info_property(self):
		self.assertEquals(self.meta_data.propert, "og:property")

	def test_info_name(self):
		self.assertEquals(self.meta_data.content, "jesnvkjsdnvk")

	def test_URl_is_stored(self):
		self.assertEquals(self.url1 in self.URldata, True)

	def test_info_is_stored(self):
		self.assertEquals(self.meta_data in self.infodata, True)