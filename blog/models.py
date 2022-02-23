from email.quoprimime import body_check
from operator import truediv
from statistics import mode
from turtle import title
from unicodedata import name
from django.db import models
from ckeditor.fields import RichTextField 
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = RichTextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='posts')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)