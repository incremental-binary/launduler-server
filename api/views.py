# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .serializers import MachineSerializer, PlaceSerializer, MachineUserSerializer, ReservationSerializer, FailureSerializer, UserguideSerializer, AlternativeSerializer
from .models import Machine, Place, MachineUser,Reservation, Failure, Userguide, Alternative

# Create your views here.
class MachineView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    # permission_classes = (IsAuthenticated,)
    serializer_class = MachineSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new machine."""
        serializer.save()

    def get_queryset(self):
        """By parameters"""
        queryset = Machine.objects.all()
        serialNum = self.request.query_params.get('serialNum', None)
        location = self.request.query_params.get('location', None)
        inUse = self.request.query_params.get('inUse', None)
        isBroken = self.request.query_params.get('isBroken', None)
        
        if serialNum is not None:
            queryset = queryset.filter(serialNum=serialNum)
        if location is not None:
            queryset = queryset.filter(location=location)
        if inUse is not None:
            queryset = queryset.filter(inUse=inUse)
        if isBroken is not None:
            queryset = queryset.filter(isBroken=isBroken)

        return queryset

class MachineDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    # permission_classes = (IsAuthenticated,)
 
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer

class PlaceView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    # permission_classes = (IsAuthenticated,)
    serializer_class = PlaceSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new place."""
        serializer.save()

    def get_queryset(self):
        """By parameters"""
        queryset = Place.objects.all()
        location = self.request.query_params.get('location', None)
        
        if location is not None:
            queryset = queryset.filter(location=location)

        return queryset

class PlaceDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    # permission_classes = (IsAuthenticated,)
 
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer

class MachineUserView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    # permission_classes = (IsAuthenticated,)
    queryset = MachineUser.objects.all()
    serializer_class = MachineUserSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new MachineUser."""
        serializer.save()

class MachineUserDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    # permission_classes = (IsAuthenticated,)
 
    queryset = MachineUser.objects.all()
    serializer_class = MachineUserSerializer

class ReservationView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    # permission_classes = (IsAuthenticated,)
    serializer_class = ReservationSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new Reservation."""
        serializer.save()

    def get_queryset(self):
        """By parameters"""
        queryset = Reservation.objects.all()
        machine = self.request.query_params.get('machine', None)
        userId = self.request.query_params.get('userId', None)
        
        if machine is not None:
            queryset = queryset.filter(machine=machine)
        if userId is not None:
            queryset = queryset.filter(userId=userId)

        return queryset

class ReservationDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    # permission_classes = (IsAuthenticated,)
 
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

class FailureView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    # permission_classes = (IsAuthenticated,)
    serializer_class = FailureSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new Failure."""
        serializer.save()
		
    def get_queryset(self):
        """By parameters"""
        queryset = Failure.objects.all()
        machine = self.request.query_params.get('machine', None)
        type = self.request.query_params.get('type', None)
        reporterId = self.request.query_params.get('reporterId', None)
        
        if machine is not None:
            queryset = queryset.filter(machine=machine)
        if type is not None:
            queryset = queryset.filter(type=type)
        if reporterId is not None:
            queryset = queryset.filter(reporterId=reporterId)

        return queryset

class FailureDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    # permission_classes = (IsAuthenticated,)
 
    queryset = Failure.objects.all()
    serializer_class = FailureSerializer

class UserguideView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    # permission_classes = (IsAuthenticated,)
    queryset = Userguide.objects.all()
    serializer_class = UserguideSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new Userguide."""
        serializer.save()

class UserguideDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    # permission_classes = (IsAuthenticated,)
 
    queryset = Userguide.objects.all()
    serializer_class = UserguideSerializer

class AlternativeView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    # permission_classes = (IsAuthenticated,)
 
    queryset = Alternative.objects.all()
    serializer_class = AlternativeSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new Alternative."""
        serializer.save()

class AlternativeDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    # permission_classes = (IsAuthenticated,)

    queryset = Alternative.objects.all()
    serializer_class = AlternativeSerializer

