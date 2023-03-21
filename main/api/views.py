from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from rest_framework.decorators import APIView,api_view
from .serializers import AccountSerializer
from ..models import Account
from rest_framework.response import Response


class Registerview(generics.CreateAPIView):
    query_set=Account.objects.all()
    serializer_class=AccountSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls,user):
        token=super().get_token(user)
        token['username']=user.username

        return token

class MyTokenObtainPairview(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

@api_view(['GET'])
def getRoutes(request):
    routes=[
        '/api/token',
        '/api/token/refresh'
    ]

    return Response(routes)
