# Generated by Django 3.0 on 2021-09-02 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0010_auto_20210901_2212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='message',
            field=models.TextField(default=False),
        ),
    ]
