# Generated by Django 3.0 on 2021-09-02 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0014_auto_20210902_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='video',
            field=models.FileField(default=False, null=True, upload_to='media/video/%y'),
        ),
    ]
