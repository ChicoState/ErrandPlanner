from django import forms
from django.core import validators
from django.contrib.auth.models import User




class JoinForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'size': '30'}))
    class Meta():
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')
        help_texts = {
            'username': None
            }

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())


# Errand validators
# Bare bones check that street address starts with a number.
# ~~ More functionality needed ~~
def validate_location(value):
    if (not value[0].isdigit()):
        raise forms.ValidationError("Please enter a valid address.")

# Errand entry form
# ~~ validators still need work ~~
class ErrandForm(forms.Form):
    title=forms.CharField(min_length=1, max_length=20, strip=True, label="Title",
        widget=forms.TextInput(attrs={'placeholder':'Grocery Shop', 'style':'width:60px'}))
    priority=forms.IntegerField(min_length=0, max_length=1, strip=True, label="Priority",
        widget=forms.TextInput(attrs={'placeholder':'1', 'style':'width:60px'}),
        validators=[validators.MaxLengthValidator(1)])
    streetaddr=forms.CharField(min_length=0, max_length=20, strip=True, label="Street Address",
        widget=forms.TextInput(attrs={'placeholder':'1234 Sesame Street', 'style':'width:60px'}),
        validators=[validators.MinLengthValidator(6)])
    city=forms.CharField(min_length=3, max_length=20, strip=True, label="City",
        widget=forms.TextInput(attrs={'placeholder':'Sunnyville', 'style':'width:60px'}),
        validators=[validators.MinLengthValidator(3)])
    state=forms.CharField(min_length=2, max_length=2, strip=True, label="State",
        widget=forms.TextInput(attrs={'placeholder':'CA', 'style':'width:60px'}),
        validators=[validators.MaxLengthValidator(2)])
    zip=forms.IntegerField(min_length=5, max_length=10, strip=True, label="Zip Code",
        widget=forms.TextInput(attrs={'placeholder':'85358', 'style':'width:60px'}),
        validators=[validators.MaxLengthValidator(10), validators.MinLengthValidator(3)])
    duration=forms.CharField(min_length=2, max_length=2, strip=True, label="Duration Est.",
        widget=forms.TextInput(attrs={'placeholder':'', 'style':'width:60px'}),
        validators=[validators.MaxLengthValidator(10)]) # this needs to change depending on how date/time are handled
