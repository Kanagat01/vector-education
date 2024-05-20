# Generated by Django 5.0.2 on 2024-05-12 07:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_users', '0006_usermodel_photo_alter_usermodel_photo_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='day_streak',
            field=models.IntegerField(default=0, verbose_name='Дневная серия'),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='last_login_datetime',
            field=models.DateTimeField(auto_now=True, verbose_name='Последний вход'),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='max_day_streak',
            field=models.IntegerField(default=0, verbose_name='Максимальная дневная серия'),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='points',
            field=models.IntegerField(default=0, verbose_name='Баллы'),
        ),
        migrations.CreateModel(
            name='UserActivityDateModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activity_dates', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Активность пользователя',
                'verbose_name_plural': 'Активности пользователей',
            },
        ),
        migrations.CreateModel(
            name='UserPointAddHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.IntegerField()),
                ('description', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='point_add_history', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'История добавления баллов',
                'verbose_name_plural': 'Истории добавления баллов',
            },
        ),
    ]