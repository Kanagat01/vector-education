# Generated by Django 5.0.2 on 2024-05-23 00:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_lessons', '0029_filltextcomponent_matchingcomponentelement_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audiocomponent',
            name='lesson_page',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_component', to='api_lessons.lessonpageelement', verbose_name='Страница урока'),
        ),
        migrations.AlterField(
            model_name='bluecardcomponent',
            name='lesson_page',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_component', to='api_lessons.lessonpageelement', verbose_name='Страница урока'),
        ),
        migrations.AlterField(
            model_name='filltextcomponent',
            name='lesson_page',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_component', to='api_lessons.lessonpageelement', verbose_name='Страница урока'),
        ),
        migrations.AlterField(
            model_name='imagecomponent',
            name='lesson_page',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_component', to='api_lessons.lessonpageelement', verbose_name='Страница урока'),
        ),
        migrations.AlterField(
            model_name='matchingcomponent',
            name='lesson_page',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_component', to='api_lessons.lessonpageelement', verbose_name='Страница урока'),
        ),
        migrations.AlterField(
            model_name='putinordercomponent',
            name='lesson_page',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_component', to='api_lessons.lessonpageelement', verbose_name='Страница урока'),
        ),
        migrations.AlterField(
            model_name='questioncomponent',
            name='lesson_page',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_component', to='api_lessons.lessonpageelement', verbose_name='Страница урока'),
        ),
        migrations.AlterField(
            model_name='recordaudiocomponent',
            name='lesson_page',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_component', to='api_lessons.lessonpageelement', verbose_name='Страница урока'),
        ),
        migrations.AlterField(
            model_name='textcomponent',
            name='lesson_page',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_component', to='api_lessons.lessonpageelement', verbose_name='Страница урока'),
        ),
        migrations.AlterField(
            model_name='videocomponent',
            name='lesson_page',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_component', to='api_lessons.lessonpageelement', verbose_name='Страница урока'),
        ),
    ]
