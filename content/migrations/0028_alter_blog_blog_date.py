# Generated by Django 3.2.7 on 2021-10-01 15:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0027_alter_blog_blog_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blog_date',
            field=models.DateField(default=datetime.datetime(2021, 10, 1, 18, 28, 49, 651385)),
        ),
    ]