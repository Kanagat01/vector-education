# Generated by Django 5.0.2 on 2024-06-16 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_users', '0020_alter_usermodel_managers_usermodel_timezone_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermodel',
            name='timezone_type',
        ),
        migrations.AddField(
            model_name='usermodel',
            name='timezone_difference',
            field=models.IntegerField(default=0, verbose_name='Разница во времени'),
        ),
    ]
