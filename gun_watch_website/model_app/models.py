# models.py

from django.db import models

class LocationCoordinates(models.Model):
    state = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()

class LocationData(models.Model):
    location = models.CharField(max_length=255)
    amount = models.IntegerField()
