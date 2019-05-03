from django.test import TestCase
from django.test import Client


class BlogTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index_view(self):
        response = self.client.get("")
        self.assertEqual(response.status_code, 200)
