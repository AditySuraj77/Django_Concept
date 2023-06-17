from django.db import models

class Fruit(models.Model):
    name = models.CharField(max_length=50)
    season = models.CharField(max_length=50)
    desc = models.TextField()
# Create your models here.
