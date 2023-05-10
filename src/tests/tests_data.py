from django.test import TestCase, Client
from django.contrib.auth.models import User
from datetime import datetime
from pytz import utc
from app.models import Event
from django.contrib.messages import get_messages
from app import models
from django.urls import reverse
from app.views import delete_errand


class ClientTestCase(TestCase):
    def test_Errand_str(self):
        testClient = Client()
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
        event.save()
        gotten = models.Event.objects.filter(
            id = event.id)
        eventid = gotten[0].id
        url = 'errands/' + str(eventid)
        newurl = reverse(delete_errand, args = [eventid])
        response = testClient.get(newurl, data={'pk':eventid})
        print(response.status_code)
        print(url)
        
        gotten = models.Event.objects.filter(
            id = eventid)
        self.assertEqual(len(gotten), 0)
