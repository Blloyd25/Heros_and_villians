from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from heroes_villians_project.super_types.serializer import Super_Types_Serializer
from .models import Super_Types
from super_types import serializer


@api_view(['GET','POST'])
def super_type_list(request):


    if request.method == 'GET':
            super_types = Super_Types.objects.all()
            serializer = Super_Types_Serializer(super_types, many=True)   
            return Response (serializer.data)

    elif request.method == 'POST':
            serializer = Super_Types_Serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response (serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET','PUT','DELETE'])
def super_types_detail(request, pk): 
    super_types = get_object_or_404(Super_Types, pk=pk)

    if request.method =='GET':       
        serializer = Super_Types_Serializer(super_types)
        return Response(serializer.data)
    elif request.method =='PUT':
        serializer =Super_Types_Serializer(super_types, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response (serializer.data)
    elif request.method == 'DELETE':
        super_types.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

