from django.db import models
from django import forms

# Create your models here.

# create a model contains 3 fields for taking information from user.  
class search(models.Model):
	# for AppStore
	App_name = forms.CharField()
	Application_id = forms.CharField()
	# for GoogleStore
	package_name = forms.URLField()
