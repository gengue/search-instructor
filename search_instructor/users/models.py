# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.encoding import python_2_unicode_compatible
from versatileimagefield.fields import VersatileImageField


@python_2_unicode_compatible
class User(AbstractUser):
    # additional fields here
    avatar = VersatileImageField('Avatar', upload_to='images/avatars/', blank=True, null=True)

    def __str__(self):
        return self.username

class Instructor(models.Model):
    user = models.ForeignKey(User)
    faculty = models.ForeignKey('courses.Faculty')
    code = models.IntegerField(blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.user.username

# for time spamped models
# see: https://gist.github.com/gengue/67742fc58410ba1f5c84
