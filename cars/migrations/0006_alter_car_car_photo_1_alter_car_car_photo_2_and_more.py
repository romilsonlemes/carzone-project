# Generated by Django 5.1.4 on 2024-12-19 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0005_alter_car_features'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='car_photo_1',
            field=models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='car',
            name='car_photo_2',
            field=models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='car',
            name='car_photo_3',
            field=models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='car',
            name='car_photo_4',
            field=models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d/'),
        ),
    ]
