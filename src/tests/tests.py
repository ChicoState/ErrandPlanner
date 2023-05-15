from django.test import TestCase
from django.contrib.auth.models import User
from datetime import datetime
from app.models import Event

class ClientTestCase(TestCase):
    # Smoke Test
    def test_smoke(self):
        self.assertEqual(1, 1)

    def test_Event_str(self):
        email = "chicostudent@mail.csuchico.edu"
        event = Event.objects.create(
            user = email,
            title="test",
            priority=1,
            streetaddr="1234 nowhere lane",
            city="Chico",
            state="CA",
            zip=00000,
            start=datetime.now(),
            duration=5,
            deadline=datetime.now(),
            scheduled=True,
            is_completed=False,
        )
        data = event.__str__()
        self.assertEqual(data, "test (" + email + ")")
