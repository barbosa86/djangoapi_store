from django.db import models
from django.db.models.base import Model
from django.db.models.fields import FloatField

# Create your models here.

class Store(models.Model):
    StoresId = models.AutoField(primary_key=True)
    StoresName = models.CharField(max_length=500)
    Latitude= models.FloatField()
    Longitude = models.FloatField()
    
    