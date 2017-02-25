from __future__ import unicode_literals
from django.db import models
import re
import bcrypt
Email_Regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
Name_Regex = re.compile(r'^[A-Za-z]+$')
# Create your models here.

class UserManager(models.Manager):
    def register(self, postData):
        errors = []
        if not Email_Regex.match(postData['email']):
            errors.append('Invalid Email')
        if len(User.objects.filter(email=postData['email']))>0:
            errors.append('Email already exists')
        if postData['password'] != postData ['confirm_password']:
            errors.append('Passwords must match')
        if len(postData['first_name'])<2:
            errors.append('First Name is too short...')
        if len(postData['last_name'])<2:
            errors.append('Last Name is too short...')
        if not Name_Regex.match(postData['first_name']):
            errors.append('First Name is not allowed to conatin numbers or symbols')
        if not Name_Regex.match(postData['last_name']):
            errors.append('Last Name is not allowed to conatin numbers or symbols')
        if len(postData['password'])<8:
            errors.append('Password must be more than 8 characters')
        if len(errors) == 0: #If there are no errors in the fomr, lets creater the user..
            newuser = User.objects.create(first_name= postData['first_name'], last_name= postData['last_name'], email= postData['email'], password= bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt()))
            return (True, newuser)
        else:
            return (False, errors)

    def login(self, postData):
        errors = []
        if 'email' in postData and 'password' in postData:
            try:
                user = User.objects.get(email=postData['email'])#userManage accesses the database using .get (finds that one user's object)
            except User.DoesNotExist:
                errors.append("Must enter a valid email and password")
                return (False, errors)

            #password check
            pw_match = bcrypt.hashpw(postData['password'].encode(), user.password.encode())
            if pw_match == user.password:
                return (True, user)
            else:
                errors.append("Invalid password")
                return (False, errors)

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class SecretManager(models.Manager):
    def validate(self, postSecret, user):
        errors = []
        if len(postSecret['content']) == 0:
            errors.append('Secret cannot be blank')
        if len(errors) == 0:
            newmessage = Secret.Secretmanager.create(content=postData['content'], user = user)
            return (True, newmessage)
        else:
            return (False, errors)

class Secret(models.Model):
    content = models.CharField(max_length=255)
    creator = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    Secretmanager = SecretManager()
