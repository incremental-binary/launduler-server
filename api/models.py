# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Machine(models.Model):
    """This class represents the machine model."""
    name = models.CharField(max_length=255, blank=False, unique=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)