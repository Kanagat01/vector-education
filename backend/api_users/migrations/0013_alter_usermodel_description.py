# Generated by Django 5.0.2 on 2024-05-23 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_users', '0001_squashed_0012_alter_usermodel_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
    ]
