# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.timezone import now
from django.db import models

# Create your models here.

class Pictures(models.Model):
    primarykey = models.CharField(max_length=200,null=False)
    filename = models.CharField(max_length=200,default='')
    path = models.CharField(max_length=200,default='')
    fullpath=models.CharField(max_length=400,default='')
    selectcount = models.IntegerField(default=0)
    last_used = models.DateTimeField(null=True)
    removed = models.BooleanField(default=False)
    favorite = models.BooleanField(default=False)
