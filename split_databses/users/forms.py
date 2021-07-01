from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User, Post


class UserAuthForm(forms.ModelForm):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)
    
    class Meta:
    	model = User
    	fields = ['username', 'password']



class UserPostForm(forms.ModelForm):

	class Meta:
		model = Post
		fields = ['user', 'text']