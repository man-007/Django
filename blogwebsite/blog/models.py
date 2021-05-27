from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
from django.urls import reverse

class Post(models.Model):

	title = models.CharField(max_length=100)
	Author = models.ForeignKey(User, on_delete=models.CASCADE)
	Description = models.TextField()
	posted_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk':self.pk})
