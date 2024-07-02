# Generated by Django 5.0.2 on 2024-07-02 01:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_additional_materials', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='additionallessonelement',
            name='image_component',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='additional_lesson_element', to='api_additional_materials.additionalimagecomponent'),
        ),
        migrations.AlterField(
            model_name='additionallessonelement',
            name='video_component',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='additional_lesson_element', to='api_additional_materials.additionalvideocomponent'),
        ),
    ]