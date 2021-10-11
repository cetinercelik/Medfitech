# Generated by Django 3.2.7 on 2021-09-30 09:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0014_auto_20210930_1126'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'verbose_name': 'Blog Haberleri Ekle', 'verbose_name_plural': 'Blog Haberleri Ekle'},
        ),
        migrations.AlterModelOptions(
            name='imagepost',
            options={'verbose_name': 'Slider İçerik Ekle', 'verbose_name_plural': 'Slider İçerik Ekle'},
        ),
        migrations.RemoveField(
            model_name='imagepost',
            name='home',
        ),
        migrations.AlterField(
            model_name='blog',
            name='blog_date',
            field=models.DateField(default=datetime.datetime(2021, 9, 30, 12, 24, 29, 160788)),
        ),
    ]