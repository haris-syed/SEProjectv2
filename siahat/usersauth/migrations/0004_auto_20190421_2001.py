# Generated by Django 2.1.7 on 2019-04-21 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersauth', '0003_auto_20190330_1101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='_type',
            field=models.CharField(choices=[('standard', 'standard'), ('hotel_owner', 'hotel_owner'), ('restaurant_owner', 'restaurant_owner')], default='male', max_length=7),
        ),
    ]
