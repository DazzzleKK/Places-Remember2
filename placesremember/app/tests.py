from django.test import TestCase, Client
from django.urls import reverse

# Create your tests here.


class TestView(TestCase):
    def test_list_GET(self):
        client = Client()

        response = client.get(reverse("list"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "app/list.html")
