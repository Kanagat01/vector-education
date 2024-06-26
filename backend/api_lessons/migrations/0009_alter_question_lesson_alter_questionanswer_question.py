# Generated by Django 5.0.2 on 2024-05-06 22:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_lessons', '0008_alter_lessonbatch_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='lesson',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='api_lessons.lesson', verbose_name='Урок'),
        ),
        migrations.AlterField(
            model_name='questionanswer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='api_lessons.question', verbose_name='Вопрос'),
        ),
    ]
