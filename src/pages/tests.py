from django.test import TestCase


class ViewTests(TestCase):
    def test_home_page(self):
        """Home page should respond with a success 200."""
        response = self.client.get("/", follow=True)
        self.assertEqual(response.status_code, 200)
