from django.shortcuts import render
from rest_framework.generics import CreateAPIView,ListAPIView
from .api.serializers import AccountSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Account

# Create your views here.


class UserRegister(CreateAPIView):
    serializer_class=AccountSerializer
    def post(self,request):
        serializer=AccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



class Userprofile(ListAPIView):
    queryset=Account.objects.all()
    serializer_class=AccountSerializer
    # def put(self,request,id):
    #     user=request.user
    #     profile=Account.objects.get(username=user,pk=id)
    #     serializer=AccountSerializer(profile,data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)

    def get(self,request):
        user=request.user
        if user:
            profile=Account.objects.get(username=user)
            print(profile)
            serializer=AccountSerializer(profile,many=False)
            
            return Response(serializer.data)
        return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)
            

        

