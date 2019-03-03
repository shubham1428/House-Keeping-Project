from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django.utils import timezone
from enum import Enum
# Create your models here.

class FrequencyChoice(Enum):
    HOURLY = "hourly"
    DAILY = "daily"
    WEEKLY = "weekly"
    MONTHLY = "monthly"
    YEARLY = "yearly"

class Asset(models.Model):
    assetname = models.CharField(max_length=200)
    
    def __str__(self):
        return self.assetname

class Task(models.Model):
    assetid = models.ForeignKey('hkmanagement.Asset',on_delete=models.CASCADE, related_name= "tasks")
    taskname = models.CharField(max_length=200)
    frequency = models.CharField(
        max_length=10,
        choices = [(ch.name,ch.value) for ch in FrequencyChoice],
    )
    
    def __str__(self):
        return self.taskname

class Admin(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Worker(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class TaskAssignment(models.Model):
    assetid = models.ForeignKey('hkmanagement.Asset')
    taskid = models.ForeignKey('hkmanagement.Task')
    workerid = models.ForeignKey('hkmanagement.Worker')
    timeOfAllocation = models.DateTimeField(default = timezone.now)
    taskToBePerformedBy = models.DateTimeField()