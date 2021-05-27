from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
# Create your views here.
from .models import Post

from django.views.generic import (
	ListView, 
	DetailView, 
	CreateView,
	UpdateView,
	DeleteView
	)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def home(request):
	context={
		'posts':Post.objects.all()

	}

	return render(request,'home.html', context)

class PostListView(ListView):
	model = Post
	template_name = 'home.html'
	context_object_name = 'posts'
	paginate_by = 2
	order_by = ['-posted_date']
	

class UserPostListView(ListView):
	model = Post
	template_name = 'blog/user_post.html'
	context_object_name = 'posts'
	paginate_by = 2

	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return Post.objects.filter(Author = user).order_by('-posted_date')

class PostDetailView(DetailView):
	model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	fields = ['title','Description']

	def form_valid(self, form):
		form.instance.Author = self.request.user
		return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	fields = ['title', 'Description']

	def form_valid(self,form):
		form.instance.Author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.Author:
			return True
		else:
			return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	success_url = '/'

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.Author:
			return True
		else:
			return False


def about(request):
	return render(request, 'about.html', {'title' : 'About'})

