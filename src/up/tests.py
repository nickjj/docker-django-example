from django.test import TestCase


class ViewTests(TestCase):
    def test_up(self):
        """Up should respond with a success 200."""
        response = self.client.get("/up/", follow=True)
        self.assertEqual(response.status_code, 200)

    def test_up_databases(self):
        """Up databases should respond with a success 200."""
        response = self.client.get("/up/databases", follow=True)
        self.assertEqual(response.status_code, 200)
