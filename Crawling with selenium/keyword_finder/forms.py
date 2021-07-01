from .models import URl
from django import forms

# create a form inorder to take url from user.
class url_form(forms.ModelForm):
	site_url = forms.CharField()
	class Meta:
		model = URl
		fields = ['site_url']