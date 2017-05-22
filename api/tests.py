# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .models import Machine

from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse

# Create your tests here.
class ModelTestCase(TestCase):
    """This class defines the test suite for the machine model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.machine_name = "Sejong-7-3F"
        self.machine = Machine(name=self.machine_name)

    def test_model_can_create_a_machine(self):
        """Test the machine model can create a machine."""
        old_count = Machine.objects.count()
        self.machine.save()
        new_count = Machine.objects.count()
        self.assertNotEqual(old_count, new_count)

class ViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.machine_data = {'name': 'Sejong-7-3F'}
        self.response = self.client.post(
            reverse('create'),
            self.machine_data,
            format="json")

    def test_api_can_create_a_machine(self):
        """Test the api has machine creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_a_machine(self):
        """Test the api can get a given machine."""
        machine = Machine.objects.get()
        response = self.client.get(
            reverse('details'),
            kwargs={'pk': machine.id}, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, machine)

    def test_api_can_update_machine(self):
        """Test the api can update a given machine."""
        change_machine = {'name': 'Sejong-7-3F'}
        res = self.client.put(
            reverse('details', kwargs={'pk': machine.id}),
            change_machine, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_machine(self):
        """Test the api can delete a machine."""
        machine = Machine.objects.get()
        response = self.client.delete(
            reverse('details', kwargs={'pk': machine.id}),
            format='json',
            follow=True)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)