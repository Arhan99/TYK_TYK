# Generated by Django 2.2.19 on 2021-03-12 18:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('create_profile', '0051_auto_20210312_1951'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='createbusiness',
            name='attitude_animals',
        ),
        migrations.RemoveField(
            model_name='createbusiness',
            name='attitude_smok',
        ),
        migrations.RemoveField(
            model_name='createbusiness',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='createbusiness',
            name='gender_neighb',
        ),
        migrations.RemoveField(
            model_name='createbusiness',
            name='presence_animals',
        ),
        migrations.RemoveField(
            model_name='createbusiness',
            name='presence_flat',
        ),
    ]
