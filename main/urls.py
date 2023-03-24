from django.urls import path
from . import views

urlpatterns=[
       
       path('register/',views.UserRegister.as_view(),name='register'),
       path('userprofile/',views.Userprofile.as_view(),name='Userprofile'),
]