# Generated by Django 3.0 on 2021-09-01 16:42

import chat.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0009_auto_20210901_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='images',
            field=models.ImageField(default=False, upload_to=chat.models.upload_image_to),
        ),
    ]