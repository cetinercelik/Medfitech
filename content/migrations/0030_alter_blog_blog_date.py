# Generated by Django 3.2.7 on 2021-10-01 16:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0029_auto_20211001_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blog_date',
            field=models.DateField(default=datetime.datetime(2021, 10, 1, 19, 9, 42, 369470)),
        ),
    ]