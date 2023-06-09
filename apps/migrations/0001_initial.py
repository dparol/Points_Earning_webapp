# Generated by Django 4.1.7 on 2023-03-22 14:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Socialapp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_name', models.CharField(max_length=200)),
                ('app_link', models.URLField()),
                ('app_category', models.CharField(choices=[('entertaiment', 'ENTERTAIMENT'), ('utility', 'UTILITY'), ('travel', 'TRAVEL'), ('Lifestyle', 'LIFESTYLE'), ('Game', 'GAME'), ('business', 'Business'), ('education', 'EDUCATION')], max_length=100)),
                ('sub_cat', models.CharField(choices=[('social', 'SOCIAL_MEDIA'), ('e-commerce', 'E-COMMERCE'), ('streaming', 'Streaming')], max_length=50)),
                ('points', models.IntegerField()),
                ('app_img', models.ImageField(upload_to='')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='UsermakePoints',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('screen_shot', models.ImageField(upload_to='')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('app', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.socialapp')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
