from rest_framework import serializers
from .models import Socialapp,UsermakePoints,Totalpoints

class SocialappSerializer(serializers.ModelSerializer):
    class Meta:
        model=Socialapp
        fields='__all__'

class Usermakepointserializer(serializers.ModelSerializer):
    class Meta:
        model=UsermakePoints
        fields=['screen_short']


class Totalpointsserializer(serializers.ModelSerializer):
    class Meta:
        model=Totalpoints
        fields="__all__"