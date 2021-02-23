from django.db import models

# Create your models here.
class Progs(models.Model):
    language_name = models.CharField(max_length = 100)
    description = models.TextField(blank = True)
    rating = models.CharField(max_length = 100)
    date_created = models.CharField(max_length = 100, blank = True)


class Review(models.Model):
    review = models.CharField(max_length = 100)
    username = models.CharField(max_length = 100) #FK to link to user table
    langname = models.CharField(max_length = 100, blank= True) #FK to link to progs table
    rating_no = models.CharField(max_length = 100)
    date_created = models.DateTimeField(auto_now_add= True)
  
class Users(models.Model):
    name = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)
    user_created = models.DateTimeField(auto_now_add= True)
  
