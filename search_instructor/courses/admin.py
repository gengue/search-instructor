# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.contrib import admin
from .models import Faculty, Course



class FacultyAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'slug',)
    prepopulated_fields = {'slug': ('name',), }

class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'faculty', 'slug',)
    prepopulated_fields = {'slug': ('name',), }

admin.site.register(Faculty, FacultyAdmin)
admin.site.register(Course, CourseAdmin)
