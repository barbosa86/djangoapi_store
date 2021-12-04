from django.db import models

class Stores(models.Model):
    StoresId = models.AutoField(primary_key=True)
    StoresName = models.CharField(max_length=500)
    Latitude= models.FloatField()
    Longitude = models.FloatField()
    
    def __str__(self) -> str:
        return self.StoresName