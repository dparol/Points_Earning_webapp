from django.db import models

# Create your models here.


cat_choice=(
    ('entertaiment','ENTERTAIMENT'),
    ('utility','UTILITY'),
    ('travel','TRAVEL'),
    ('Lifestyle','LIFESTYLE'),
    ('Game','GAME'),
    ('business','SOCIAL_MEDIA'),
    ('education','EDUCATION'),
)

sub_cate=(
    ('social','SOCIAL_MEDIA'),
    ('food',''),
    ('travel',''),
    ('music',''),
    ('fitness',''),
)


class Socialapp(models.Model):
    app_name=models.CharField(max_length=200)
    app_link=models.URLField(max_length=200)
    app_category=models.CharField(max_length=100,choices=cat_choice)
    sub_cat=models.CharField(max_length=50,choices=sub_cat)