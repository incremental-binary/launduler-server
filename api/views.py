# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from rest_framework import generics
from .serializers import MachineSerializer
from .models import Machine

# Create your views here.
class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new machine."""
        serializer.save()

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = Machine.objects.all()
    serializer_class = MachineSerializer