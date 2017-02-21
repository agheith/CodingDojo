from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=45) #create columns here ..'first_name'
    last_name = models.CharField(max_length=45)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
class Post(models.Model):
    title = models.CharField(max_length=45)
    message = models.TextField(max_length=1000)
    # Notice the association made with ForeignKey for a one-to-many relationship
    user_id = models.ForeignKey(User) #equivalent to clicking on the many table to the one table on the workbench
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

# run the migrations!!

#python manage.py makemigrations
#python manage.py migrate
