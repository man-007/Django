from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserAuthForm, UserPostForm
from .models import User

context={}
for ele in User.objects.all(): 
	context[ele.username] = ele.password 
# Create your views here.
def home(request):
	if request.POST:
		form = UserAuthForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			if username in context.keys():
				if password == context[username]:
					return redirect('post')
				else:
					messages.info(request, f'Please enter correct Password!')
					return redirect('home')
			else:
				messages.info(request, f'{username} not exist!')
				return redirect('home')
	else:
		form = UserAuthForm()

	return render(request, 'home.html', {'form':form})

def post(request):
	if request.method == "POST":
		form = UserPostForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, f'Post has been saved!')
			return redirect('home')

		else:
			messages.info(request, f'Please enter correct details!')

	else:
		form = UserPostForm()

	return render(request, 'post.html', {'form':form})