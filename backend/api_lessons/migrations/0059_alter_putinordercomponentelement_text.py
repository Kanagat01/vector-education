# Generated by Django 5.0.2 on 2024-06-27 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_lessons', '0058_alter_userlessonmodel_review_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='putinordercomponentelement',
            name='text',
            field=models.CharField(max_length=2048, verbose_name='Текст элемента'),
        ),
    ]
