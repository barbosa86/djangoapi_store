from random import random

from rest_framework import serializers

from StoresApp.models import Stores


class StoresSerializers(serializers.ModelSerializer):
    class Meta:
        model=Stores
        fields=('StoresId, StoresName, Latitude, Longitude')
