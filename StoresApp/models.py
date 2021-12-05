from django.db import models


class Stores(models.Model):
    StoresId = models.AutoField(primary_key=True)
    StoresName = models.CharField(max_length=500)
    Latitude = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    Longitude = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)

    # @property
    # def my_field(self):
    #     return 2+2

    def __str__(self):
        return self.StoresName
