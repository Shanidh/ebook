from django.db import models

# Create your models here.
class User(models.Model):
    username=models.CharField(max_length=10, unique=True)
    password=models.CharField(max_length=10)

#ebook table
class Ebook(models.Model):
    title = models.CharField(max_length=20)
    author = models.CharField(max_length=20)
    genre = models.CharField(max_length=20)
    review = models.IntegerField()
    favourite = models.BooleanField()
    fkUser = models.ForeignKey(User,on_delete=models.CASCADE,null=True)

# to store token when login
class Usertoken(models.Model):
    token = models.CharField(max_length=1000)
    fkUser = models.ForeignKey(User,on_delete=models.CASCADE,null=True)