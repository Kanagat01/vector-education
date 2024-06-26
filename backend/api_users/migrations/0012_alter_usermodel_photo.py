# Generated by Django 5.0.2 on 2024-05-20 22:46

import api_users.models
import protected_media.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_users', '0011_alter_useractivitydatemodel_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='photo',
            field=protected_media.models.ProtectedImageField(blank=True, null=True, storage=protected_media.models.ProtectedFileSystemStorage(), upload_to=api_users.models.PathAndRename('user_photos/'), verbose_name='Фото'),
        ),
    ]
