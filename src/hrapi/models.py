# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from enumerify import fields

from django.db import models

from django.utils import timezone

from django.core.exceptions import ValidationError

from .enums import LocationType

# Create your models here.

class Project(models.Model):

    name = models.CharField(max_length=100, null=False)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.name
    
    
class Log(models.Model):
    owner=models.ForeignKey('auth.User',related_name='logs',on_delete=models.CASCADE)
    project = models.ForeignKey(Project, related_name='projects_log', on_delete=models.CASCADE, null=True, blank=True)
    task_date = models.DateTimeField(default=timezone.now)
    location = fields.SelectIntegerField(
        blueprint=LocationType, default=LocationType.INSIDE)
    details = models.TextField(blank=True)
    working_hour = models.FloatField(blank=False, null=False, default='0.00')
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        if self.location == 1:
            return "INSIDE"
        return "OUTSIDE"
    
    def save(self, *args, **kwargs):
        if self.task_date.date() < timezone.now().date():
            raise ValidationError("The task date cannot be in the past!")
        elif self.task_date.date() > timezone.now().date():
            raise ValidationError("The task date cannot be in the future!")
        super(Log, self).save(*args, **kwargs)