from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=100)


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=100)
