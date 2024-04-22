# Generated by Django 5.0.2 on 2024-04-22 14:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('api_base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuizBatch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=2000, verbose_name='Название')),
                ('card_color', models.CharField(choices=[('blue', 'Синий'), ('green', 'Зеленый')], max_length=100, verbose_name='Цвет карточки')),
            ],
            options={
                'verbose_name': 'Викторина',
                'verbose_name_plural': 'Викторины',
            },
        ),
        migrations.CreateModel(
            name='SurveyQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=2000, verbose_name='Вопрос')),
            ],
            options={
                'verbose_name': 'Опрос: вопрос',
                'verbose_name_plural': 'Опрос: вопросы',
            },
        ),
        migrations.CreateModel(
            name='QuizQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=100, verbose_name='Вопрос')),
                ('quiz_batch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='api_tasks.quizbatch', verbose_name='Викторина')),
            ],
            options={
                'verbose_name': 'Вопрос викторины',
                'verbose_name_plural': 'Вопросы викторины',
            },
        ),
        migrations.CreateModel(
            name='QuizQuestionAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=2000, verbose_name='Ответ')),
                ('is_correct', models.BooleanField(default=False, verbose_name='Правильный ответ')),
                ('quiz_question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='api_tasks.quizquestion', verbose_name='Вопрос')),
            ],
            options={
                'verbose_name': 'Ответ на вопрос викторины',
                'verbose_name_plural': 'Ответы на вопросы викторины',
            },
        ),
        migrations.CreateModel(
            name='UserTasksProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('survey_completed', models.BooleanField(default=False, verbose_name='Опрос пройден')),
                ('earned_coins', models.IntegerField(default=0, verbose_name='Заработанные монеты c задании')),
                ('curr_streak', models.IntegerField(default=0, verbose_name='Нынешняя серия правильных ответов')),
                ('max_streak', models.IntegerField(default=0, verbose_name='Максимальная серия правильных ответов')),
                ('completed_quizzes', models.ManyToManyField(related_name='completed_users', to='api_tasks.quizbatch', verbose_name='Пройденные викторины')),
                ('user_profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='tasks_profile', to='api_base.userprofile', verbose_name='Профиль пользователя')),
            ],
            options={
                'verbose_name': 'Пользователь Задании',
                'verbose_name_plural': 'Пользователи Задании',
            },
        ),
        migrations.CreateModel(
            name='UserSurveyAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark', models.IntegerField(default=False, verbose_name='Оценка')),
                ('survey_question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='api_tasks.surveyquestion', verbose_name='Вопрос')),
                ('user_tasks_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='survey_answers', to='api_tasks.usertasksprofile', verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Опрос: ответ',
                'verbose_name_plural': 'Опрос: ответы',
            },
        ),
        migrations.CreateModel(
            name='UserQuizQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coins_earned', models.IntegerField(default=0, verbose_name='Заработанные монеты')),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_tasks.quizquestionanswer', verbose_name='Ответ')),
                ('quiz_question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_answers', to='api_tasks.quizquestion', verbose_name='Вопрос')),
                ('user_tasks_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quiz_questions', to='api_tasks.usertasksprofile', verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Ответ на вопрос викторины',
                'verbose_name_plural': 'Ответы на вопросы викторины',
            },
        ),
    ]
