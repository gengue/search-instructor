# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('created', models.DateTimeField(verbose_name='fecha de creacion', auto_now_add=True)),
                ('modified', models.DateTimeField(verbose_name='fecha de modificacion', auto_now=True)),
                ('name', models.CharField(max_length=140)),
                ('slug', autoslug.fields.AutoSlugField(unique_with=('name', 'faculty'))),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('created', models.DateTimeField(verbose_name='fecha de creacion', auto_now_add=True)),
                ('modified', models.DateTimeField(verbose_name='fecha de modificacion', auto_now=True)),
                ('name', models.CharField(max_length=140)),
                ('code', models.IntegerField(null=True, blank=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='course',
            name='faculty',
            field=models.ForeignKey(to='courses.Faculty'),
        ),
    ]
