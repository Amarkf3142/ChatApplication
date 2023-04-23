# Generated by Django 3.0 on 2021-09-03 10:43

import chat.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0017_auto_20210902_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='images',
            field=models.ImageField(blank=True, default=False, null=True, upload_to=chat.models.upload_image_to),
        ),
        migrations.AlterField(
            model_name='message',
            name='video',
            field=models.FileField(blank=True, default=False, null=True, upload_to=chat.models.upload_image_to),
        ),
    ]
