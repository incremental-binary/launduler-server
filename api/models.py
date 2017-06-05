# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Place(models.Model):
    """This class represents the place model."""
    location = models.CharField(max_length=255, blank=False, unique=True)

    # ps. We have to decide data type, how to represent
    operationTime = models.CharField(max_length=255)
    def __str__(self):
        return "{}".format(self.location)

class MachineUser(models.Model):
    """This class represents the alternative service model."""
    userId = models.CharField(max_length=255, blank=False, unique=True)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    location = models.ForeignKey(Place, to_field="location")

    def __str__(self):
        return "{}".format(self.userId)

class Machine(models.Model):
    """This class represents the machine model."""
    serialNum = models.CharField(max_length=255, blank=False, unique=True)
    #location = models.CharField(max_length=255, blank=False, default='none')
    location = models.ForeignKey(Place, to_field="location")
    inUse = models.BooleanField(default=False)
    isBroken = models.BooleanField(default=False)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.serialNum)
		
class Reservation(models.Model):
    """This class represents the alternative service model."""
    machine = models.ForeignKey(Machine, to_field="serialNum")
    date = models.CharField(max_length=255)
    userId = models.ForeignKey('auth.user', to_field="username")

    def __str__(self):
        return "{}".format(self.machine)

class Failure(models.Model):
    """This class represents the failure model."""
    machine = models.ForeignKey(Machine, to_field="serialNum")
    type = models.CharField(max_length=255, blank=False, default='none')
    comment = models.TextField()
    reporterId = models.ForeignKey('auth.user', to_field="username")
    isFixed = models.BooleanField(default=False)

    def __str__(self):
        return "{}".format(self.machine)

class Userguide(models.Model):
    """This class represents the userguide model."""
    guideName = models.CharField(max_length=255, blank=False, unique=True, default='none')
    content = models.TextField()

    def __str__(self):
        return "{}".format(self.guideName)

class Alternative(models.Model):
    """This class represents the alternative service model."""
    name = models.CharField(max_length=255, blank=False, unique=True, default='none')
    description = models.CharField(max_length=255)
    link = models.CharField(max_length=255)

    def __str__(self):
        return "{}".format(self.serviceName)
