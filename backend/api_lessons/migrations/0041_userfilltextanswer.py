# Generated by Django 5.0.2 on 2024-05-24 20:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_lessons', '0040_remove_filltextline_put_words_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserFillTextAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=2000, verbose_name='Ответ')),
                ('line', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='api_lessons.filltextline', verbose_name='Строка')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fill_text_answers', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Ответ на строку компонента заполните текст',
                'verbose_name_plural': 'Ответы на строки компонента заполните текст',
            },
        ),
    ]