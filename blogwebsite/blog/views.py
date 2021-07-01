from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# importing user model(pre defined in the framework). 
from django.contrib.auth.models import User

from .models import Post

# Importing generic views for allowing class based views. 
from django.views.generic import (
	ListView, 
	DetailView, 
	CreateView,
	UpdateView,
	DeleteView
	)
# Importing the mixins tags(used for restrictions).
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def home(request):
	context={
		'posts':Post.objects.all()

	}

	return render(request,'home.html', context)

# CLASS VIEWS

# view for front page.
class PostListView(ListView):
	model = Post
	template_name = 'home.html'
	context_object_name = 'posts'
	paginate_by = 2
	order_by = ['-posted_date']
	
# view for Users itself posts.
class UserPostListView(ListView):
	model = Post
	template_name = 'blog/user_post.html'
	# naming of the variable through which we can iterate. 
	context_object_name = 'posts'
	# Pagination
	paginate_by = 2		

	# Getting all the post of user itself.  
	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return Post.objects.filter(Author = user).order_by('-posted_date')

# view for detail view of the post. 
class PostDetailView(DetailView):
	model = Post

# Creating the Posts
class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	fields = ['title','Description']

	# for validation of form. 
	def form_valid(self, form):
		form.instance.Author = self.request.user
		return super().form_valid(form)

# Updating the Post
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	fields = ['title', 'Description']

	# form validation
	def form_valid(self,form):
		form.instance.Author = self.request.user
		return super().form_valid(form)

	# Allow only user to update their profile. 
	def test_func(self):
		post = self.get_object()
		if self.request.user == post.Author:
			return True
		else:
			return False

# Deleting the Post
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	success_url = '/'

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.Author:
			return True
		else:
			return False


# about page. 
def about(request):
	return render(request, 'about.html', {'title' : 'About'})

