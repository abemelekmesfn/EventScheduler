from django.test import TestCase
from .models import Event
from django.contrib.auth import get_user_model
from datetime import datetime, timedelta

User = get_user_model()

class EventTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="eventuser", password="password123")
        self.event = Event.objects.create(
            title="Meeting",
            description="Team meeting",
            location="Office",
            start_time=datetime.now(),
            end_time=datetime.now() + timedelta(hours=1),
            organizer=self.user
        )

    def test_event_creation(self):
        self.assertEqual(self.event.title, "Meeting")
