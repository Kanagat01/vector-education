# Generated by Django 5.0.2 on 2024-05-10 05:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_lessons', '0010_alter_question_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConspectusComponent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Конспект', max_length=200, verbose_name='Заголовок')),
                ('text', models.TextField(verbose_name='Текст')),
            ],
            options={
                'verbose_name': 'Конспект',
                'verbose_name_plural': 'Конспекты',
            },
        ),
        migrations.CreateModel(
            name='VideoComponent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=2000, verbose_name='Описание')),
                ('video_url', models.URLField(verbose_name='Ссылка на видео')),
            ],
            options={
                'verbose_name': 'Видео компонент',
                'verbose_name_plural': 'Видео компоненты',
            },
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='description',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='video_url',
        ),
        migrations.RenameModel(
            old_name='Question',
            new_name='QuestionComponent',
        ),
        migrations.CreateModel(
            name='LessonComponent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('video', 'Видео'), ('question', 'Вопрос'), ('conspectus', 'Конспект')], max_length=20, verbose_name='Тип компонента')),
                ('order', models.PositiveIntegerField(verbose_name='Порядок')),
                ('conspectus_component', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api_lessons.conspectuscomponent')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='components', to='api_lessons.lesson', verbose_name='Урок')),
                ('question_component', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api_lessons.questioncomponent')),
                ('video_component', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api_lessons.videocomponent')),
            ],
            options={
                'verbose_name': 'Компонент урока',
                'verbose_name_plural': 'Компоненты уроков',
                'ordering': ['order'],
            },
        ),
    ]
