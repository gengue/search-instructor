# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.contrib import admin
from .models import Lesson, TimeInterval, Session, Like



class LessonAdmin(admin.ModelAdmin):
    list_display = ('instructor', 'course', 'is_official', 'price', 'description', 'created', 'modified',)

class SessionAdmin(admin.ModelAdmin):
    list_display = ('day', 'time_interval', 'lesson',)

class TimeIntervalAdmin(admin.ModelAdmin):
    list_display = ('start_time', 'close_time',)

class LikeAdmin(admin.ModelAdmin):
    list_display = ('lesson', 'user',)

admin.site.register(Lesson, LessonAdmin)
admin.site.register(Session, SessionAdmin)
admin.site.register(TimeInterval, TimeIntervalAdmin)
admin.site.register(Like, LikeAdmin)
