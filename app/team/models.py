from django.db import models
from tinymce.models import HTMLField



class Player(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    detail = HTMLField()   # creating text editor on admin panel


# Create your models here.
