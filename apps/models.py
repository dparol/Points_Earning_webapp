from django.db import models
from main.models import Account

# Create your models here.


cat_choice=(
    ('entertaiment','ENTERTAIMENT'),
    ('utility','UTILITY'),
    ('travel','TRAVEL'),
    ('Lifestyle','LIFESTYLE'),
    ('Game','GAME'),
    ('business','Business'),
    ('education','EDUCATION'),
)

sub_cate=(
    ('social','SOCIAL_MEDIA'),
    ('e-commerce','E-COMMERCE'),
    ('streaming','Streaming'),
    
)


class Socialapp(models.Model):
    
    app_name=models.CharField(max_length=200)
    app_link=models.URLField(max_length=200)
    app_category=models.CharField(max_length=100,choices=cat_choice)
    sub_cat=models.CharField(max_length=50,choices=sub_cate)
    points=models.IntegerField()
    app_img=models.ImageField(upload_to='images')

    created_date=models.DateTimeField(auto_now_add=True)

class UsermakePoints(models.Model):
    user=models.ForeignKey(Account,on_delete=models.CASCADE,null=True,blank=True)
    app=models.ForeignKey(Socialapp,on_delete=models.CASCADE)
    screen_shot=models.ImageField()
    created_time=models.DateTimeField(auto_now_add=True)

class Totalpoints(models.Model):
    user=models.ForeignKey(UsermakePoints,on_delete=models.CASCADE)
    total=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)