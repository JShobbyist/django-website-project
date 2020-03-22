from django.db import models
from datetime import date

# Create your models here.
class Articles(models.Model):
    id = models.AutoField(primary_key=True)
    classif = models.CharField(max_length=30)
    headline = models.CharField(max_length=255)
    content = models.TextField()
    reporter = models.CharField(max_length=100)
    img_path = models.CharField(max_length=50)
    date = models.DateField(auto_now=False)

class Events(models.Model):
    id = models.AutoField(primary_key=True)
    headline = models.CharField(max_length=255)
    date = models.DateField(auto_now=False)
    classif = models.CharField(max_length=30)
    learnmore = models.TextField()
    img_path = models.CharField(max_length=50)

class News(models.Model):
    id = models.AutoField(primary_key=True)
    headline = models.CharField(max_length=255)
    date = models.DateField(auto_now=False)
    content = models.TextField()
    img_path = models.CharField(max_length=50)