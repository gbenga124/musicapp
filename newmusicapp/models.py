from pyexpat import model
from turtle import title
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Artiste(models.model):
    firstname=models.CharField(_MAX_LENGTH,400)
    lastname=models.CharField(_MAX_LENGTH,400) 
    age=models.IntegerField
    Artisteid=models.CharField(_MAX_LENGTH,50)
class song(models.Model):
    title=models.CharField(_MAX_LENGTH,400)
    datereleased=models.DateField
    likes=models.IntegerField
    Artisteid=models.CharField(_MAX_LENGTH,50)
    songid=models.CharField(_MAX_LENGTH,50)
class lyric(models.model):
    songid=models.CharField(_MAX_LENGTH,50)
    content=models.CharField(_MAX_LENGTH,200)
