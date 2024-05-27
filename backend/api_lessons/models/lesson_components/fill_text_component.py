from typing import Type

from django.contrib import admin
from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe

from api_users.models import UserModel
from .__component_base import ComponentBase


class FillTextComponent(ComponentBase):
    title = models.CharField(max_length=200, verbose_name='Заголовок', default='Заполните текст')
    put_words = models.BooleanField(default=False, verbose_name='Перетаскивание слов')

    class Meta:
        verbose_name = 'Заполните текст компонент'
        verbose_name_plural = 'Заполните текст компоненты'

    def __str__(self):
        return f'{self.pk} FillTextComponent: "{self.title}"'


class FillTextLine(models.Model):
    component = models.ForeignKey(FillTextComponent, on_delete=models.CASCADE, verbose_name='Компонент',
                                  related_name='lines')
    text_before = models.CharField(max_length=10000, verbose_name='Текст', null=True, blank=True)
    answer = models.CharField(max_length=2000, verbose_name='Ответ (оставьте пустым если только текст )', null=True,
                              blank=True)
    text_after = models.CharField(max_length=10000, verbose_name='Текст после', null=True, blank=True)
    order = models.PositiveIntegerField(default=0, verbose_name='Порядок')

    class Meta:
        verbose_name = 'Строка компонента заполните текст'
        verbose_name_plural = 'Строки компонента заполните текст'

    def save(self, *args, **kwargs):
        if self.component.lines.filter(order=self.order).exclude(pk=self.pk).exists():
            raise ValueError('Order must be unique in component')
        if self.put_words and not self.answer:
            raise ValueError('Answer must be filled if put_words is True')
        if not self.text_after and not self.text_before:
            raise ValueError('At least one of text_before or text_after must be filled')
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.pk} FillTextLineComponent'


class UserFillTextAnswer(models.Model):
    user = models.ForeignKey('api_users.UserModel', on_delete=models.CASCADE, verbose_name='Пользователь',
                             related_name='fill_text_answers')
    line = models.ForeignKey(FillTextLine, on_delete=models.CASCADE, verbose_name='Строка', related_name='answers')
    answer = models.CharField(max_length=2000, verbose_name='Ответ')

    class Meta:
        verbose_name = 'Ответ на строку компонента заполните текст'
        verbose_name_plural = 'Ответы на строки компонента заполните текст'

    def __str__(self):
        return f'{self.pk} UserFillTextAnswer: "{self.answer}"'