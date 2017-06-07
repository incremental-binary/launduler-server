# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from rest_framework import serializers
from .models import Machine, Failure, Userguide, Alternative, Place, Reservation
from rest_auth.registration.serializers import RegisterSerializer

class ReservationSerializer(serializers.ModelSerializer):

    scheduledAt = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False)
    class Meta:
        model = Reservation
        fields = ('id', 'machine', 'scheduledAt', 'userId')

class MachineSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    reservations = serializers.SerializerMethodField('get_reservation')
    isBroken = serializers.SerializerMethodField() #'get_isBroken' is redundant

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Machine
        fields = ('id', 'serialNum', 'location', 'inUse', 'isBroken' ,'reservations')
        read_only_fields = ()

    def get_reservation(self, machine):
        fdate = datetime.today()
        fdate = fdate.replace(hour=0, minute=0, second=0, microsecond=0)
        items =Reservation.objects.filter(scheduledAt__gte = fdate, machine=machine)
        serializer = ReservationSerializer(instance=items, many=True)
        return serializer.data

    def get_isBroken(self, machine):
        items = Failure.objects.filter(machine=machine, isFixed=False)
        if items.count() == 0:
            return False
        else:
            return True

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
        fields = ('id', 'name', 'description', 'link')


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ('id', 'location', 'operationTime')

#class MachineUserSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = MachineUser
#        fields = ('id', 'userId', 'email', 'password', 'name', 'location')


#class RegistrationSerializer(RegisterSerializer):
    #first_name = serializers.CharField(required=True)
    #last_name = serializers.CharField(required=True)

#    def get_cleaned_data(self):
#        return {
#            'username': self.validated_data.get('username', ''),
#            'password': self.validated_data.get('password', ''),
#            'email': self.validated_data.get('email', '')
#        }
