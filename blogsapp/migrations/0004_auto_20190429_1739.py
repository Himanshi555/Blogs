# Generated by Django 2.2 on 2019-04-29 12:09

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogsapp', '0003_auto_20190429_1653'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='reply',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='replies', to='blogsapp.Comment'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='date_and_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 29, 17, 39, 47, 132223)),
        ),
    ]
