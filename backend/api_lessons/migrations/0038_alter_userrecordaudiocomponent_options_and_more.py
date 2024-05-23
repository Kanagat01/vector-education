# Generated by Django 5.0.2 on 2024-05-23 03:40

import backend.global_function
import protected_media.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_lessons', '0037_rename_bluecard_component_lessonpageelement_blue_card_component_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userrecordaudiocomponent',
            options={'verbose_name': 'Записи пользователей аудио компонент', 'verbose_name_plural': 'Записи пользователей аудио компоненты'},
        ),
        migrations.AlterField(
            model_name='imagecomponent',
            name='image',
            field=protected_media.models.ProtectedImageField(storage=protected_media.models.ProtectedFileSystemStorage(), upload_to=backend.global_function.PathAndRename('images/'), verbose_name='Изображение'),
        ),
    ]
