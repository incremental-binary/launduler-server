# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Machine(models.Model):
    """This class represents the machine model."""
    serialNum = models.CharField(max_length=255, blank=False, unique=True)
    location = models.CharField(max_length=255, blank=False, default='none')
    inUse = models.BooleanField(default=False)
    isBroken = models.BooleanField(default=False)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)

class Failure(models.Model):
    """This class represents the failure model."""
    machine = models.CharField(max_length=255, blank=False, default='none')
    type = models.CharField(max_length=255, blank=False, default='none')
    comment = models.TextField()
    reporterId = models.CharField(max_length=255)
    isFixed = models.BooleanField(default=False)

    def __str__(self):
        return "{}".format(self.name)

class Userguide(models.Model):
    """This class represents the userguide model."""
    guideName = models.CharField(max_length=255, blank=False, default='none')
    content = models.TextField()

    def __str__(self):
        return "{}".format(self.name)

class Alternative(models.Model):
    """This class represents the alternative service model."""
    serviceName = models.CharField(max_length=255, blank=False, default='none')
    location = models.CharField(max_length=255)
    phoneNum = models.CharField(max_length=255)
    price = models.CharField(max_length=255)

    def __str__(self):
        return "{}".format(self.name)
