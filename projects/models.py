from concurrent.futures import process
from email.mime import image
from operator import mod
from pydoc import describe
from pyexpat import model
from turtle import title
from django.db import models
from ckeditor.fields import RichTextField 
from django.urls import reverse

# Create your models here.
class Technology(models.Model):
    name = models.CharField(max_length=180)
    image = models.FilePathField(path="C:\Development\mwilliamson_portfolio_python\mwilliamson_portfolio_python\img", default=None,blank=True, null=True)
class Category(models.Model):
    name = models.CharField(max_length=180)
    image = models.FilePathField(path="C:\Development\mwilliamson_portfolio_python\mwilliamson_portfolio_python\img", default=None,blank=True, null=True)
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    #technology = models.CharField(max_length=20)
    image = models.FilePathField(path="C:\Development\mwilliamson_portfolio_python\mwilliamson_portfolio_python\img", default=None,blank=True, null=True)
    about = RichTextField(default=None, blank=True, null=True)
    my_role = RichTextField(default=None, blank=True, null=True)
    metrics = RichTextField(default=None, blank=True, null=True)
    process = RichTextField(default=None, blank=True, null=True)
    result = RichTextField(default=None, blank=True, null=True)
    technologies = models.ManyToManyField(Technology)
    slug = models.SlugField(null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'slug': self.slug}) # new
    
