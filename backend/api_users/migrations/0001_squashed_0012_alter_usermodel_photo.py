# Generated by Django 5.0.2 on 2024-05-23 04:19

import backend.global_function
import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
import protected_media.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [('api_users', '0001_initial'), ('api_users', '0002_alter_usermodel_friendship_requests'), ('api_users', '0003_usermodel_user_type_alter_usermodel_description_and_more'), ('api_users', '0004_remove_usermodel_image_usermodel_photo_url'), ('api_users', '0005_alter_usermodel_description'), ('api_users', '0006_usermodel_photo_alter_usermodel_photo_url'), ('api_users', '0007_usermodel_day_streak_usermodel_last_login_datetime_and_more'), ('api_users', '0008_alter_usermodel_last_login_datetime'), ('api_users', '0009_remove_usermodel_last_login_datetime_and_more'), ('api_users', '0010_alter_userpointaddhistory_created_date'), ('api_users', '0011_alter_useractivitydatemodel_options'), ('api_users', '0012_alter_usermodel_photo')]

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Email')),
                ('description', models.TextField(default='No Bio Yet', verbose_name='Описание')),
                ('firebase_user_id', models.CharField(blank=True, max_length=200, null=True)),
                ('fcm_token', models.CharField(blank=True, max_length=255, null=True)),
                ('blocked', models.BooleanField(default=False)),
                ('friends', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, verbose_name='Друзья')),
                ('friendship_requests', models.ManyToManyField(blank=True, related_name='pending_friend_requests', to=settings.AUTH_USER_MODEL, verbose_name='Запросы в друзья')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
                ('user_type', models.CharField(choices=[('free', 'Бесплатный'), ('paid', 'Оплаченный'), ('premium_paid', 'Премиум оплаченный')], default='free', max_length=20)),
                ('photo_url', models.URLField(blank=True, null=True, verbose_name='Ссылка на фото (Firebase)')),
                ('photo', protected_media.models.ProtectedImageField(blank=True, null=True, storage=protected_media.models.ProtectedFileSystemStorage(), upload_to=backend.global_function.PathAndRename('user_photos/'), verbose_name='Фото')),
                ('day_streak', models.IntegerField(default=0, verbose_name='Дневная серия')),
                ('max_day_streak', models.IntegerField(default=0, verbose_name='Максимальная дневная серия')),
                ('points', models.IntegerField(default=0, verbose_name='Баллы')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='NotificationSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('periodic_lesson_reminders', models.BooleanField(default=True)),
                ('friend_request_notifications', models.BooleanField(default=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserPointAddHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.IntegerField()),
                ('description', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата добавления')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='point_add_history', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'История добавления баллов',
                'verbose_name_plural': 'Истории добавления баллов',
            },
        ),
        migrations.CreateModel(
            name='UserActivityDateModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата активности')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activity_dates', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Активность пользователя',
                'verbose_name_plural': 'Активности пользователей',
                'ordering': ['-datetime'],
            },
        ),
    ]
