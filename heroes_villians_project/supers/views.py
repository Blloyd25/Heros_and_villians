from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import Supers_Serializer
from .models import Supers
from supers import serializers





@api_view(['GET','POST'])
def supers_list(request):

    if request.method == 'GET':
            supers = Supers.objects.all()
            serializer = Supers_Serializer(supers, many=True)   
            return Response (serializer.data)

    elif request.method == 'POST':
            serializer = Supers_Serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response (serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET','PUT','DELETE'])
def supers_detail(request, pk): 
    supers = get_object_or_404(Supers, pk=pk)

    if request.method =='GET':       
        serializer = Supers_Serializer(supers)
        return Response(serializer.data)
    elif request.method =='PUT':
        serializer =Supers_Serializer(supers, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response (serializer.data)
    elif request.method == 'DELETE':
        supers.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
