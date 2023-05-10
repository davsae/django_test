from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import Arts_test
from api.models import Orders
from api.serializers import Art_Serializer
from api.serializers import Orders_Serializer
from django.http import HttpResponseBadRequest

@api_view(['GET'])
def my_api(request):
    data = Arts_test.objects.all()
    return Response(data)
#//////////////////////////////////////////Articulos//////////////////////////////////////
@api_view(['GET'])
def get_art(request, pk):
    art = Arts_test.objects.get(pk=pk)
    serializer = Art_Serializer(art)
    return Response(serializer.data)

@api_view(['POST'])
def create_art(request):
    serializer = Art_Serializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return HttpResponseBadRequest()
    

@api_view(['PUT'])
def update_art(request, pk):
    user = Art_Serializer.objects.get(pk=pk)
    serializer = Art_Serializer(instance=user, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)
    
#//////////////////////////////////////////Ordenes//////////////////////////////////////
@api_view(['GET'])
def get_order(request, pk):
    art = Orders_Serializer.objects.get(pk=pk)
    serializer = Orders_Serializer(art)
    return Response(serializer.data)

@api_view(['POST'])
def create_order(request):
    serializer = Orders_Serializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return HttpResponseBadRequest()
    
@api_view(['PUT'])
def update_order(request, pk):
    user = Orders_Serializer.objects.get(pk=pk)
    serializer = Orders_Serializer(instance=user, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)