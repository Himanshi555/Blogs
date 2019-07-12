# Generated by Django 2.2 on 2019-04-29 11:23

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogsapp', '0002_auto_20190423_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='Description',
            field=models.TextField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='blog',
            name='date_and_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 29, 16, 53, 33, 507006)),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('Email', models.EmailField(max_length=225)),
                ('comment', models.TextField()),
                ('date_and_time', models.DateTimeField(auto_now_add=True)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogsapp.Blog')),
            ],
        ),
    ]