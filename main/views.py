from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from .api.serializers import AccountSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class UserRegister(CreateAPIView):
    serializer_class=AccountSerializer
    def post(self,request):
        serializer=AccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        

# class UserLogin()