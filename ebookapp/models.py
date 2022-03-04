from django.db import models

# Create your models here.
class Ebook(models.Model):
    title = models.CharField(max_length=20)
    author = models.CharField(max_length=20)
    genre = models.CharField(max_length=20)
    review = models.CharField(max_length=10)
    favourite = models.CharField(max_length=10)