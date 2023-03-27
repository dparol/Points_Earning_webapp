from django.shortcuts import render
from rest_framework.generics import CreateAPIView,ListCreateAPIView
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from rest_framework.decorators import permission_classes,api_view

from .serializers import SocialappSerializer,Usermakepointserializer,Totalpointsserializer
from rest_framework.response import Response

from .models import Socialapp,UsermakePoints,Totalpoints
from main.models import Account
from django.db.models import Sum

# Create your views here.



# @permission_classes([IsAuthenticated])
class CreateNew_app(CreateAPIView):
    queryset=Socialapp.objects.all()
    serializer_class=SocialappSerializer

    def post(self,request):
        data=request.data
        print(data)
        appname=data['app_name']
        app_link=data['app_link']
        app_category=data['app_category']
        sub_cat=data['sub_cat']
        points=data['points']
        app_img=data['app_img']
        print(appname)
        newapp=Socialapp.objects.create(
            app_name=appname,
            app_link=app_link,
            app_category=app_category,
            sub_cat=sub_cat,
            points=points,
            app_img=app_img,

        )
        serializer=SocialappSerializer(newapp,many=False)
        return Response(serializer.data)


class ListAllapps(ListCreateAPIView):
    queryset=Socialapp.objects.all()
    serializer_class=SocialappSerializer

    def get(self,request):
        data=Socialapp.objects.all()
        serializer=SocialappSerializer(data,many=True)
        return Response(serializer.data)


class createpoints(ListCreateAPIView):
    queryset=UsermakePoints.objects.all()
    
    serializer_class=Usermakepointserializer

    def post(self,request,id):
        
        data=request.data
        currentuser=data['user']
        print(currentuser)
        user=Account.objects.get(username=currentuser)
        print(user)
        
        app=Socialapp.objects.get(id=id)
        print(app)

        image=data['screen_shot']
        print(image)

        makenewpoint=UsermakePoints.objects.create(
            user=user,
            app=app,
            screen_shot=image


        )

        serializer=Usermakepointserializer(makenewpoint,many=False)
        return Response(serializer.data)



class Totalpoints(ListCreateAPIView):
    queryset=Totalpoints.objects.all()
    serializer_class=Totalpointsserializer

    def get(self,request):

        currentuser=request.user
        user=UsermakePoints.objects.filter(user__username=currentuser)
        total=user.aggregate(total_points=Sum('app__points'))
        print(total)
        return Response(total)

