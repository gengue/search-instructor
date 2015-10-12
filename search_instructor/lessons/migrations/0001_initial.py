# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0002_auto_20151012_0131'),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('created', models.DateTimeField(verbose_name='fecha de creacion', auto_now_add=True)),
                ('modified', models.DateTimeField(verbose_name='fecha de modificacion', auto_now=True)),
                ('is_official', models.BooleanField(default=True)),
                ('price', models.IntegerField(default=0)),
                ('description', models.TextField(blank=True)),
                ('course', models.ForeignKey(to='courses.Course')),
                ('instructor', models.ForeignKey(to='users.Instructor')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('created', models.DateTimeField(verbose_name='fecha de creacion', auto_now_add=True)),
                ('modified', models.DateTimeField(verbose_name='fecha de modificacion', auto_now=True)),
                ('lesson', models.ForeignKey(to='lessons.Lesson')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('created', models.DateTimeField(verbose_name='fecha de creacion', auto_now_add=True)),
                ('modified', models.DateTimeField(verbose_name='fecha de modificacion', auto_now=True)),
                ('day', models.IntegerField()),
                ('lesson', models.ForeignKey(to='lessons.Lesson')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TimeInterval',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('start_time', models.TimeField()),
                ('close_time', models.TimeField()),
            ],
        ),
        migrations.AddField(
            model_name='session',
            name='time_interval',
            field=models.ForeignKey(to='lessons.TimeInterval'),
        ),
    ]
