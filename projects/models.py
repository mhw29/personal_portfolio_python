from email.mime import image
from operator import mod
from pydoc import describe
from pyexpat import model
from turtle import title
from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.FilePathField(path="C:\Development\mwilliamson_portfolio_python\mwilliamson_portfolio_python\img")
    