# Generated by Django 2.2.19 on 2021-03-12 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('create_profile', '0050_auto_20210312_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createbusiness',
            name='attitude_animals',
            field=models.CharField(choices=[('1', 'положительное'), ('2', 'нейтральное'), ('3', 'отрицательное')], max_length=15, verbose_name='Отношение к животным'),
        ),
        migrations.AlterField(
            model_name='createbusiness',
            name='attitude_smok',
            field=models.CharField(choices=[('1', 'положительное'), ('2', 'нейтральное'), ('3', 'отрицательное')], max_length=15, verbose_name='Отношение к курящему'),
        ),
        migrations.AlterField(
            model_name='createbusiness',
            name='sel_city',
            field=models.CharField(choices=[('1', 'Москва'), ('2', 'Красноярск'), ('3', 'Ачинск'), ('4', 'Абакан'), ('5', 'Дивногорск'), ('6', 'Сосновоборск')], max_length=15, verbose_name='Выбрать город'),
        ),
        migrations.AlterField(
            model_name='createbusiness',
            name='sel_distr',
            field=models.CharField(choices=[('1', 'Кировский'), ('2', 'Ленинский'), ('3', 'Октябрьский'), ('4', 'Свердловский'), ('5', 'Советский'), ('6', 'Центральный'), ('7', 'Железнодорожный')], max_length=15, verbose_name='Выбрать район'),
        ),
    ]
