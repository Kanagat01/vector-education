# Generated by Django 5.0.2 on 2024-05-31 15:40

import backend.global_function
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_lessons', '0047_alter_userfilltextanswer_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userrecordaudiocomponent',
            name='file',
            field=models.FileField(upload_to=backend.global_function.PathAndRename(path='record_component_answer/'), verbose_name='Аудио файл'),
        ),
    ]