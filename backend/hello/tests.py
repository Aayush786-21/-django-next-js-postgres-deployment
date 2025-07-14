from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Greeting

# Create your tests here.

class GreetingAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.greeting = Greeting.objects.create(message="Hello Test!")

    def test_hello_api(self):
        url = reverse('api_hello')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('message', response.data)

    def test_list_greetings(self):
        url = reverse('greeting-list-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) >= 1)

    def test_create_greeting(self):
        url = reverse('greeting-list-create')
        data = {'message': 'New Greeting'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['message'], 'New Greeting')

    def test_retrieve_greeting(self):
        url = reverse('greeting-detail', args=[self.greeting.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], self.greeting.message)

    def test_update_greeting(self):
        url = reverse('greeting-detail', args=[self.greeting.id])
        data = {'message': 'Updated Greeting'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], 'Updated Greeting')

    def test_delete_greeting(self):
        url = reverse('greeting-detail', args=[self.greeting.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
