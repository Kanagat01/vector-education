# Generated by Django 5.0.2 on 2024-05-14 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_lessons', '0018_alter_userlessonmodel_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lesson',
            options={'ordering': ['order'], 'verbose_name': 'Урок', 'verbose_name_plural': 'Уроки'},
        ),
        migrations.AddField(
            model_name='lesson',
            name='order',
            field=models.IntegerField(default=1, verbose_name='Порядок урока в коллекции'),
            preserve_default=False,
        ),
    ]