# Generated by Django 5.0.2 on 2024-05-08 04:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_data_collection', '0002_remove_dcquestionanswer_answered_users_dcuseranswer'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dcuseranswer',
            options={'verbose_name': 'Ответ пользователя (Дата коллекция)', 'verbose_name_plural': 'Ответы пользователей (Дата коллекция)'},
        ),
    ]
