from __future__ import unicode_literals
from django.contrib import messages
from django.db import models
import re

# Create your models here.
class UserManager(models.Manager):
    def validate(self, postData):
        status = True
        errors = []
        if len(postData['name'])<1:
            errors.append('Must enter a name')
        if len(postData['interest'])<1:
            errors.append('Must enter an interest')
        if len(User.objects.filter(name = postData['name']))>0:
            if len(User.objects.filter(name=postData['name']).filter(interest__name=postData['interest'])) > 0:
                errors.append('Someone already has that interest')
                status = False
            else:
                 this_user = User.objects.get(name=postData['name'])
                 this_interest = Interest.objects.create(name=postData['interest'])
                 this_user.interests.add(this_interest)
                 errorlist.append('User already registered!')
                 status = False
        if status == False:
            return {'errors': errorlist}
        else:
            print 'hi'
            this_user = User.objects.create(name=postData['name'])
            this_user = User.objects.get(name=postData['name'])
            this_interest = Interest.objects.create(name=postData['interest'])
            this_user.interests.add(this_interest)
            return {}


class Interest(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()


class User(models.Model):
    name = models.CharField(max_length=100)
    interests = models.ManyToManyField(Interest, related_name="users")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
