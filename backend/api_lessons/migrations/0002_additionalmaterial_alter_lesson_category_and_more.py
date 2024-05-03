# Generated by Django 5.0.2 on 2024-05-02 16:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_lessons', '0001_initial'),
        ('api_users', '0002_userprofile_notificationsettings_delete_customuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdditionalMaterial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=255)),
                ('body', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='lesson',
            name='category',
            field=models.CharField(choices=[('Listening', 'Listening'), ('Reading', 'Reading'), ('Writing', 'Writing'), ('Speaking', 'Speaking')], max_length=10),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='video',
            field=models.URLField(),
        ),
        migrations.CreateModel(
            name='Progress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('has_watched', models.BooleanField(default=False)),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_lessons.lesson')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_users.userprofile')),
            ],
        ),
        migrations.DeleteModel(
            name='LessonCategory',
        ),
    ]