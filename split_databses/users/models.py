from django.db import models

# Create your models here.
class User(models.Model):
	first_name = models.CharField("First Name", max_length=100)
	last_name = models.CharField("Last Name", max_length=100)
	email_id = models.EmailField()
	password = models.TextField()
	username = models.CharField("Username",max_length=100)

	def __str__(self):
		return self.username


class Post(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	text = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

