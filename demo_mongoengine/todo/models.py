from django.db import models
import datetime
# Create your models here.
from mongoengine import Document, StringField, DateTimeField

class todo_lis(Document):
    task = StringField(max_length=100)
    Description = StringField()
    date_added = DateTimeField(default=datetime.datetime.utcnow)