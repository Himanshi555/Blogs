# Generated by Django 2.2 on 2019-04-30 10:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogsapp', '0006_auto_20190430_1227'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='Email',
        ),
        migrations.AlterField(
            model_name='blog',
            name='date_and_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 30, 15, 48, 15, 791620)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='Name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
