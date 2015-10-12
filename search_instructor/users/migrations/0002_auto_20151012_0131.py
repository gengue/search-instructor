# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import versatileimagefield.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('code', models.IntegerField(null=True, blank=True)),
                ('phone', models.IntegerField(null=True, blank=True)),
                ('faculty', models.ForeignKey(to='courses.Faculty')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=versatileimagefield.fields.VersatileImageField(verbose_name='Avatar', upload_to='images/avatars/', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='instructor',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
