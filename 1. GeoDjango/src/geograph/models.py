from django.contrib.gis.db import models

# Create your models here.

class Agent(models.Model):
    name = models.CharField(max_length=100, blank=True)
    location = models.PointField()
    adress = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)

class ZI(models.Model):
    name = models.CharField(max_length=100)
    location = models.MultiPolygonField(null=True, blank=True)