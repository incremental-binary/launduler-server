# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Machine,Place,Failure,Reservation,Userguide,Alternative

admin.site.register(Machine)
#admin.site.register(MachineUser)
admin.site.register(Place)
admin.site.register(Failure)
admin.site.register(Reservation)
admin.site.register(Userguide)
admin.site.register(Alternative)

