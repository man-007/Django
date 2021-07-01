from django.db import models
# Create your models here.

# form an info model to store name, property and content of meta data in database 
class info(models.Model):
    name = models.CharField(max_length=100)
    propert = models.CharField(max_length=100)
    content = models.TextField()

# form another model to store the url and meta data. 
class URl(models.Model):
	site_url = models.TextField()
	# form Many-to-One relation so as to store multiple info of meta data with same url.
	meta_data_container = models.ForeignKey(info, on_delete=models.CASCADE)
