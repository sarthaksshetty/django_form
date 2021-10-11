from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255, default='Welcome to my Page')
    author = models.CharField(max_length=200)
    body = models.TextField()

    def __str__(self):
        return self.title + self.author
