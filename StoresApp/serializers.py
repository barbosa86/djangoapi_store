from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from StoresApp.models import stores


class StoresSerializers(serializers.ModelSerializer):
    class Meta:
        model=stores
        fields=('StoresId, StoresName, Latitude, Longitude')
