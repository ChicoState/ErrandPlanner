from django.test import TestCase
from datetime import datetime
from pytz import utc
from app.forms import ErrandForm

class ErrandTestCase(TestCase):
    #Add errand
    def test_add_errand_form(self):
        formData = {
            'title': 'test' ,
            'priority': 1, 
            'streetaddr': '1234 nowhere lane', 
            'city': 'Chico', 
            'state': 'CA', 
            'zip': 00000, 
            'duration': 5
            }
        form = ErrandForm(data = formData)
        self.assertTrue(form.is_valid())
    
    def test_add_errand_null(self):
        formData = {}
        form = ErrandForm(data = formData)
        self.assertFalse(form.is_valid())
    
    def test_add_errand_wrong_title(self):
        formData = {
            'title': 12345 ,
            'priority': 1, 
            'streetaddr': '1234 nowhere lane', 
            'city': 'Chico', 
            'state': 'CA', 
            'zip': 00000, 
            'duration': 5
            }
        form = ErrandForm(data = formData)
        self.assertFalse(form.is_valid())
    
    def test_add_errand_wrong_priority(self):
        formData = {
            'title': 'test' ,
            'priority': 'first', 
            'streetaddr': '1234 nowhere lane', 
            'city': 'Chico', 
            'state': 'CA', 
            'zip': 00000, 
            'duration': 5
            }
        form = ErrandForm(data = formData)
        self.assertFalse(form.is_valid())
    
    def test_add_errand_wrong_addr(self):
        formData = {
            'title': 'test' ,
            'priority': 1, 
            'streetaddr': 12345, 
            'city': 'Chico', 
            'state': 'CA', 
            'zip': 00000, 
            'duration': 5
            }
        form = ErrandForm(data = formData)
        self.assertFalse(form.is_valid())
    
    def test_add_errand_wrong_city(self):
        formData = {
            'title': 'test' ,
            'priority': 1, 
            'streetaddr': '1234 nowhere lane', 
            'city': 12345, 
            'state': 'CA', 
            'zip': 00000, 
            'duration': 5
            }
        form = ErrandForm(data = formData)
        self.assertFalse(form.is_valid())
    
    def test_add_errand_wrong_state(self):
        formData = {
            'title': 'test' ,
            'priority': 1, 
            'streetaddr': '1234 nowhere lane', 
            'city': 'Chico', 
            'state': 12, 
            'zip': 00000, 
            'duration': 5
            }
        form = ErrandForm(data = formData)
        self.assertFalse(form.is_valid())
    
    def test_add_errand_wrong_zip(self):
        formData = {
            'title': 'test' ,
            'priority': 1, 
            'streetaddr': '1234 nowhere lane', 
            'city': 'Chico', 
            'state': 'CA', 
            'zip': 'Here', 
            'duration': 5
            }
        form = ErrandForm(data = formData)
        self.assertFalse(form.is_valid())
    
    def test_add_errand_wrong_duration(self):
        formData = {
            'title': 'test' ,
            'priority': 1, 
            'streetaddr': '1234 nowhere lane', 
            'city': 'Chico', 
            'state': 'CA', 
            'zip': 00000, 
            'duration': 'five minutes'
            }
        form = ErrandForm(data = formData)
        self.assertFalse(form.is_valid())

    def test_add_errand_wrong_types(self):
        formData = {
            'title': 12345 ,
            'priority': 'test', 
            'streetaddr': utc.localize(datetime.now()), 
            'city': 0, 
            'state': 31, 
            'zip': 'test', 
            'duration': 'five'
            }
        form = ErrandForm(data = formData)
        self.assertFalse(form.is_valid())
    