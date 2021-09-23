from mongoengine import *
from mongoengine.base.fields import ObjectIdField
from mongoengine.document import Document
from mongoengine.fields import DateTimeField, StringField
from bson import ObjectId 
import datetime

class Task(Document):
    user = StringField()
    user_id = StringField()
    task = StringField()
    description = StringField()
    date_added = DateTimeField(default=datetime.datetime.utcnow)