# Generated by Django 2.1.7 on 2019-04-21 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siahatapp', '0008_auto_20190421_1545'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='picture',
            field=models.ImageField(default='default.jpg', upload_to='post_pictures'),
        ),
    ]
