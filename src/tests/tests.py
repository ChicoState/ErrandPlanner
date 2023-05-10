from django.test import TestCase
from django.contrib.auth.models import User
from datetime import datetime
from pytz import utc
from app.models import Event


class ClientTestCase(TestCase):
    # Smoke Test
    def test_smoke(self):
        self.assertEqual(1, 1)

    # Object Function Tests
    def test_Errand_str(self):
        user = User.objects.create_user("0", "0")
        event = Event.objects.create(
            user=user,
            title="test",
            priority=1,
            streetaddr="1234 nowhere lane",
            city="Chico",
            state="CA",
            zip=00000,
            start=utc.localize(datetime.now()),
            duration=5,
            is_errand=True,
            scheduled=True,
        )
        data = event.__str__()
        self.assertEqual(data, "Errand: test (0)")

    def test_Event_str(self):
        user = User.objects.create_user("0", "0")
        event = Event.objects.create(
            user=user,
            title="test",
            priority=1,
            streetaddr="1234 nowhere lane",
            city="Chico",
            state="CA",
            zip=00000,
            start=utc.localize(datetime.now()),
            duration=5,
            is_errand=False,
            scheduled=True,
        )
        data = event.__str__()
        self.assertEqual(data, "Event: test (0)")
