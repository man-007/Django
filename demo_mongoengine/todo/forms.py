from django import forms
from mongoengine.fields import DateField 

class add_work(forms.Form):
    task = forms.CharField()
    description = forms.CharField()
    date_added = DateField()