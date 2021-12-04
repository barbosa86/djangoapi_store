from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, viewset, status
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from StoresApp import serializers

from StoresApp.models import Stores
from StoresApp.serializers import StoresSerializers
from rest_framework.response import Response

class StoreViewSet(viewset.ViewSet):
    def list(self, request):
        queryset = Stores.objects.all()
        serializer = StoresSerializers(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Stores.objects.all()
        user = get_object_or_404(queryset, pk=pk)

        serializer = StoresSerializers(user)
        return Response(serializer.data)

    def create(self, request):
        store_serializers = StoresSerializers(data=request.data)
        store_serializers.is_valid(raise_exception=True)
        store_serializers.save()
        return Response(store_serializers.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        store = get_object_or_404(Stores, id=pk)
        store_serializers = StoresSerializers(instance=store, data=request.data)
        store_serializers.is_valid(raise_exception=True)
        store_serializers.save()
        return Response(store_serializers.data, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        store = get_object_or_404(Stores, id=pk)
        store.delete()
        return Response({'msg': 'store deleted.'}, status=status.HTTP_204_NO_CONTENT)
       

# Usando generics 

# class StoresList(generics.ListCreateAPIView):
#     queryset = Stores.objects.all()
#     serializer_class = StoresSerializers
#
# class StoresDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Stores.objects.all()
#     serializer_class = StoresSerializers

# Create your views here.

#@csrf_exempt
#def storesApi(request,id=0):
#    if request.method=='GET':
#        stores = Stores.objects.all()
#        stores_serializers=StoresSerializers(stores,many=True)
#        return JsonResponse(stores_serializers.data,safe=False)
#    elif request.method =='POST':
#        store_data=JSONParser().parse(request)
#        stores_serializers=StoresSerializers(data=store_data)
#        if stores_serializers.is_valid():
#           stores_serializers.save()
#            return JsonResponse("Added Successfully",safe=False)
#        return JsonResponse("Failed to Add", safe=False)
#    elif request.method=='PUT':
#        store_data=JSONParser().parse(request)
#        store = Stores.objects.get(StoresId=store_data['StoresId'])
#        stores_serializers=StoresSerializers(store,data=store_data)
#        if stores_serializers.is_valid():
#            stores_serializers.save()
#            return JsonResponse("Update Successfully", safe=False)
#        return JsonResponse("Failed to update")
#    elif request.method=='DELETE':
#        store = Stores.objects.get(StoresId=id)  
#        store.delete()
#        return JsonResponse("Delete Successfully", safe=False)