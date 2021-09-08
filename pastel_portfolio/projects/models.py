from django.db import models

# Create your models here.
class Porjects(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField()
    tech = models.CharField(max_length=100)
    header = models.CharField(max_length=200)
    para = models.TextField()


class Blog(models.Model):
    title = models.CharField(max_length=100)
    brief = models.CharField(max_length=200)
    image = models.ImageField()
    keys = models.CharField(max_length=100)
    header = models.CharField(max_length=200)
    para = models.TextField()