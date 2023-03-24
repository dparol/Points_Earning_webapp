from django.urls import path
from . import views
from django.conf.urls.static import static
from Assessment import settings

urlpatterns = [
    
    path('newapp/',views.CreateNew_app.as_view(),name='newapp'),
    path('listallapps/',views.ListAllapps.as_view(),name='listall'),
    path('createpoints/<int:id>',views.createpoints.as_view(),name='createpoints'),
    path('Totalpoints',views.Totalpoints.as_view(),name='Totalpoints'),


]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
