# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.db import models
from courses.models import TimeStampedModel


class Lesson(TimeStampedModel):
    instructor = models.ForeignKey('users.Instructor')
    course = models.ForeignKey('courses.Course')
    is_official = models.BooleanField(default=True)
    price = models.IntegerField(default=0)
    description = models.TextField(blank=True)

    def __str__(self):
        return ('%s - %s')%(self.instructor, self.course)

class TimeInterval(models.Model):
    start_time = models.TimeField()
    close_time = models.TimeField()

    def __str__(self):
        return ('%s - %s')%(self.start_time, self.close_time)

class Session(TimeStampedModel):
    day = models.IntegerField() # 0: lunes, 1:martes, etc
    time_interval = models.ForeignKey(TimeInterval)
    lesson = models.ForeignKey(Lesson)

class Like(TimeStampedModel):
    lesson = models.ForeignKey(Lesson)
    user = models.ForeignKey('users.User')

    def __str__(self):
        return ('%s - %s')%(self.lesson, self.user)




