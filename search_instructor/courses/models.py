# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.db import models
from autoslug import AutoSlugField


class TimeStampedModel(models.Model):
    """
    Una clase abstracta que registra la fecha de creacion y
    modificacion del modelo
    """
    created = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creacion")
    modified = models.DateTimeField(auto_now=True, verbose_name="fecha de modificacion")

    class Meta:
        abstract = True

class Faculty(TimeStampedModel):
    name = models.CharField(max_length=140)
    code = models.IntegerField(blank=True, null=True)
    slug = AutoSlugField(populate_from='name')

    def __str__(self):
        return self.name

class Course(TimeStampedModel):
    name = models.CharField(max_length=140)
    faculty = models.ForeignKey(Faculty)
    slug = AutoSlugField(unique_with=('name','faculty'))

    def __str__(self):
        return self.name
