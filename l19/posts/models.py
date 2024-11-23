from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    comments = models.IntegerField()
    likes = models.IntegerField()
    timestamp = models.DateField(auto_now=True)