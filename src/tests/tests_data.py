from django.test import TestCase
from datetime import datetime
from app.models import Event
from app import models
from django.http import HttpRequest
from app import views
from importlib import import_module
from django.conf import settings
from app.forms import ErrandForm


class ClientTestCase(TestCase):
    def setUp(self):
        request = HttpRequest()
        request.method = "POST"
        request.session = {"user": {"mail": "chicostudent@mail.csuchico.edu"}}

    def test_errand_complete_uncomplete(self):
        email = "chicostudent@mail.csuchico.edu"
        event = Event.objects.create(
            user=email,
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
            is_completed=True,
        )
        event.save()
        eventid = event.id
        request = HttpRequest()
        request.method = "GET"
        engine = import_module(settings.SESSION_ENGINE)
        session_key = None
        request.session = engine.SessionStore(session_key)
        request.session["user"] = {"mail": email}
        response = views.completeErrand(request, eventid)
        gotten = models.Event.objects.filter(id=eventid)
        self.assertEqual(gotten[0].is_completed, False)

    def test_errand_complete_complete(self):
        email = "chicostudent@mail.csuchico.edu"
        event = Event.objects.create(
            user=email,
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
        event.save()
        eventid = event.id
        request = HttpRequest()
        request.method = "GET"
        engine = import_module(settings.SESSION_ENGINE)
        session_key = None
        request.session = engine.SessionStore(session_key)
        request.session["user"] = {"mail": email}
        response = views.completeErrand(request, eventid)
        gotten = models.Event.objects.filter(id=eventid)
        self.assertEqual(gotten[0].is_completed, True)

    def test_Errand_add(self):
        email = "chicostudent@mail.csuchico.edu"
        formData = {
            "title": "test",
            "priority": 1,
            "streetaddr": "1234 nowhere lane",
            "city": "Chico",
            "state": "CA",
            "zip": 00000,
            "duration": 5,
        }
        request = HttpRequest()
        request.method = "POST"
        engine = import_module(settings.SESSION_ENGINE)
        session_key = None
        request.session = engine.SessionStore(session_key)
        request.session["user"] = {"email": email}
        request.POST = formData
        request.POST["add"] = formData
        response = views.addErrand(request)
        gotten = models.Event.objects.filter(city="Chico")
        self.assertEqual(len(gotten), 1)

    def test_Errand_edit(self):
        email = "chicostudent@mail.csuchico.edu"
        event = Event.objects.create(
            user=email,
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
        event.save()
        formData = {
            "title": "Changed",
            "priority": 1,
            "streetaddr": "1234 nowhere lane",
            "city": "Chico",
            "state": "CA",
            "zip": 00000,
            "duration": 5,
        }
        request = HttpRequest()
        request.method = "POST"
        engine = import_module(settings.SESSION_ENGINE)
        session_key = None
        request.session = engine.SessionStore(session_key)
        request.session["user"] = {"email": email}
        request.POST = formData
        request.POST["edit"] = formData
        response = views.editErrand(request, event.id)
        gotten = models.Event.objects.filter(title="Changed")
        self.assertEqual(len(gotten), 1)

    def test_Errand_delete(self):
        email = "chicostudent@mail.csuchico.edu"
        event = Event.objects.create(
            user=email,
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
        event.save()
        gotten = models.Event.objects.filter(id=event.id)
        eventid = gotten[0].id
        request = HttpRequest()
        request.method = "POST"
        engine = import_module(settings.SESSION_ENGINE)
        session_key = None
        request.session = engine.SessionStore(session_key)
        request.session["user"] = {"mail": email}
        response = views.deleteErrand(request, eventid)
        gotten = models.Event.objects.filter(id=eventid)
        self.assertEqual(len(gotten), 0)
