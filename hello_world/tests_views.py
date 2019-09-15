from django.test import TestCase
from django.test.client import RequestFactory
from .views import hello_world_json, hello_world_html

class RequestTests(TestCase):

    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()

    def test_my_view_html(self):
        request = self.factory.get('/')
        response = hello_world_html(request)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Hello, World!")

    def test_my_view_json(self):
        request = self.factory.get('/')
        response = hello_world_json(request)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '{"message": "Hello, World!"}')
