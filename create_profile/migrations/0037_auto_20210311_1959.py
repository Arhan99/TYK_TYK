# Generated by Django 2.2.19 on 2021-03-11 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('create_profile', '0036_auto_20210310_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createbusiness',
            name='image_bus',
            field=models.ImageField(upload_to='images_bus', verbose_name='Загрузить изображение'),
        ),
    ]
