from random import random

from rest_framework import serializers

from StoresApp.models import Stores


class StoresSerializers(serializers.ModelSerializer):
    # detail = serializers.SerializerMethodField('find_details')
    #
    # def find_details(self, store):
    #     return random()
    class Meta:
        model = Stores
        fields = ('StoresId', 'StoresName', 'Latitude', 'Longitude')
