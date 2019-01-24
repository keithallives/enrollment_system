# Generated by Django 2.1.5 on 2019-01-24 23:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25)),
                ('middle_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('age', models.PositiveSmallIntegerField()),
                ('birthday', models.DateField()),
                ('address', models.TextField()),
                ('phone', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('enroll_date', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]
