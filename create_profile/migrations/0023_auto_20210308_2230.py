# Generated by Django 2.2.19 on 2021-03-08 20:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('create_profile', '0022_createneighbour_user_neig'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createneighbour',
            name='user_neig',
            field=models.ForeignKey(auto_created=True, blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]