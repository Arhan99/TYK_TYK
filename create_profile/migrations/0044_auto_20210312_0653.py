# Generated by Django 2.2.19 on 2021-03-12 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('create_profile', '0043_auto_20210312_0616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createneighbour',
            name='image',
            field=models.ImageField(upload_to='images_n', verbose_name='Загрузить изображение'),
        ),
    ]
