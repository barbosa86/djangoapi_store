from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from StoresApp.models import stores
from StoresApp.serializers import StoresSerializers

# Create your views here.

@csrf_exempt
def storesApi(request,id=0):
    if request.method=='GET':
        stores = Stores.objects.all()
        stores_serializers=StoresSerializers(stores,many=True)
        return JsonResponse(stores_serializers.data,safe=False)
    elif request.method =='POST':
        store_data=JSONParser().parse(request)
        stores_serializers=StoresSerializers(data=store_data)
        if stores_serializers.is_valid():
            stores_serializers.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method=='PUT':
        store_data=JSONParser().parse(request)
        store = Stores.objects.get(StoresId=store_data['StoresId'])
        stores_serializers=StoresSerializers(store,data=store_data)
        if stores_serializers.is_valid():
            stores_serializers.save()
            return JsonResponse("Update Successfully", safe=False)
        return JsonResponse("Failed to update")
    elif request.method=='DELETE':
        store = Stores.objects.get(StoresId=id)  
        store.delete()
        return JsonResponse("Delete Successfully", safe=False)