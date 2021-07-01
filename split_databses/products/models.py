from django.db import models

# Create your models here.
class Product(models.Model):
	name = models.CharField("Name", max_length=100)
	weight = models.FloatField()
	price = models.FloatField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name
		