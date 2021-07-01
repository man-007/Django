from django import forms
from .models import search

# create form to select the store between App store and PlayStore
class Search_forms(forms.Form):
	Store = (('1', 'App Store'),('2', 'Play Store'))
	print('code inside search_forms line 1')
	store_select = forms.ChoiceField(choices=Store)
	print('code inside search_forms line 2')


# create another form to input App name and Application id for Apple AppStore site. 
class App_Search_forms(forms.ModelForm):
	App_name = forms.CharField()
	Application_id = forms.CharField()

	class Meta:
		model = search
		fields = ['App_name', 'Application_id']

# create another form to input package name for Google PlayStore site.
class Google_Search_forms(forms.ModelForm):
	package_name = forms.CharField()
	class Meta:
		model = search
		fields = ['package_name']