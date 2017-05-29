# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers
from .models import Machine, Failure, Userguide, Alternative, Place, MachineUser, Reservation

class MachineSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Machine
        fields = ('id', 'serialNum', 'location', 'inUse', 'isBroken')
        read_only_fields = ()

class FailureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Failure
        fields = ('id', 'machine', 'type', 'comment', 'reporterId', 'isFixed')

class UserguideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userguide
        fields = ('id', 'guideName', 'content')

class AlternativeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alternative
        fields = ('id', 'serviceName', 'location', 'phoneNum', 'price')


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ('id', 'location', 'operationTime')

class MachineUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MachineUser
        fields = ('id', 'userId', 'email', 'password', 'name', 'location')

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ('id', 'machine', 'date', 'userId')


