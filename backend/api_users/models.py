import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.utils.deconstruct import deconstructible
from protected_media.models import ProtectedImageField
from rest_framework.exceptions import ValidationError


@deconstructible
class PathAndRename(object):
    def __init__(self, path):
        self.path = path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        filename = f'{uuid.uuid4()}.{ext}'
        return f'{self.path}{filename}'


class UserTypes:
    free = 'free'
    paid = 'paid'
    premium_paid = 'premium_paid'

    @classmethod
    def choices(cls):
        return [
            (cls.free, 'Бесплатный'),
            (cls.paid, 'Оплаченный'),
            (cls.premium_paid, 'Премиум оплаченный'),
        ]


class UserModel(AbstractUser):
    user_type = models.CharField(max_length=20, choices=UserTypes.choices(), default=UserTypes.free, )
    blocked = models.BooleanField(default=False)
    firebase_user_id = models.CharField(max_length=200, null=True, blank=True)
    fcm_token = models.CharField(max_length=255, null=True, blank=True)  # for push notifications

    # user data
    name = models.CharField(max_length=255, verbose_name='Имя')
    email = models.EmailField(max_length=255, unique=True, verbose_name='Email')
    description = models.TextField(verbose_name='Описание')
    photo = ProtectedImageField(upload_to=PathAndRename('user_photos/'), blank=True, null=True, verbose_name='Фото')
    photo_url = models.URLField(blank=True, null=True, verbose_name='Ссылка на фото (Firebase)')

    # user social data
    friends = models.ManyToManyField("self", blank=True, verbose_name='Друзья', symmetrical=True)
    friendship_requests = models.ManyToManyField("self", blank=True, symmetrical=False,
                                                 related_name='pending_friend_requests',
                                                 verbose_name='Запросы в друзья')

    # App related stuff
    points = models.IntegerField(default=0, verbose_name='Баллы')
    day_streak = models.IntegerField(default=0, verbose_name='Дневная серия')
    max_day_streak = models.IntegerField(default=0, verbose_name='Максимальная дневная серия')

    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return f'{self.pk} Profile of {self.name}'

    def add_points(self, points: int, description: str):
        if points < 0:
            raise ValueError('Points must be positive')
        if description == '':
            raise ValueError('Description must be filled')
        self.points += points
        self.save()
        UserPointAddHistory.objects.create(user=self, points=points, description=description)

    def is_paid(self):
        return self.user_type in (UserTypes.paid, UserTypes.premium_paid)

    def send_friend_request(self, to_user):
        if (to_user != self) and (to_user not in self.friends.all()):
            if self.friendship_requests.filter(pk=to_user.pk).exists():
                self.accept_friend_request(to_user)
            else:
                to_user.friendship_requests.add(self)

    def accept_friend_request(self, from_user):
        if from_user in self.friendship_requests.all():
            self.friendship_requests.remove(from_user)
            self.friends.add(from_user)
            from_user.friends.add(self)

    def decline_friend_request(self, from_user):
        if from_user in self.friendship_requests.all():
            self.friendship_requests.remove(from_user)


class NotificationSettings(models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE)
    periodic_lesson_reminders = models.BooleanField(default=True)
    friend_request_notifications = models.BooleanField(default=True)

    def __str__(self):
        return f'Настройки Уведомлении для пользователя {self.user.username}'


class UserActivityDateModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='activity_dates')
    datetime = models.DateTimeField(default=timezone.now, verbose_name='Дата активности')

    class Meta:
        verbose_name = 'Активность пользователя'
        verbose_name_plural = 'Активности пользователей'
        ordering = ['-datetime']

    def __str__(self):
        return f'{self.pk} Activity '


class UserPointAddHistory(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='point_add_history')
    points = models.IntegerField()
    description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now, verbose_name='Дата добавления')

    class Meta:
        verbose_name = 'История добавления баллов'
        verbose_name_plural = 'Истории добавления баллов'

    def __str__(self):
        return f'{self.pk} UserPointAddHistory'
