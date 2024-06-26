# Generated by Django 5.0.2 on 2024-05-06 21:00

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_users', '0002_alter_usermodel_friendship_requests'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='user_type',
            field=models.CharField(choices=[('free', 'Бесплатный'), ('paid', 'Оплаченный'), ('premium_paid', 'Премиум оплаченный')], default='free', max_length=20),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='email',
            field=models.EmailField(max_length=255, unique=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='friends',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, verbose_name='Друзья'),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='friendship_requests',
            field=models.ManyToManyField(blank=True, related_name='pending_friend_requests', to=settings.AUTH_USER_MODEL, verbose_name='Запросы в друзья'),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='image',
            field=models.ImageField(upload_to='profile_images', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Имя'),
        ),
    ]
