from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=70)
    lastname = models.CharField(max_length=70)
    email = models.EmailField(max_length=100)

    def __str__(self):  # new
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=500)
    pub_date = models.DateTimeField()
    user = models.ManyToManyField(User)

    def __str__(self):  # new
        return self.title


class Comment(models.Model):
    content = models.CharField(max_length=150)
    pub_date = models.DateTimeField()
    comment = models.ManyToManyField(Post)
    user = models.ManyToManyField(User)

    def __str__(self):  # new
        return self.content
