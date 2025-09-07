from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()

class UserTestCase(TestCase):
    def test_create_user(self):
        user = User.objects.create_user(username="testuser", email="test@test.com", password="password123")
        self.assertEqual(user.username, "testuser")
