from django import forms
from django.core import validators
from django.contrib.auth.models import User
from app.models import Event


class JoinForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"})
    )
    email = forms.CharField(widget=forms.TextInput(attrs={"size": "30"}))

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email", "password")
        help_texts = {"username": None}


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())


# Errand validators
# Bare bones check that street address starts with a number.
# ~~ More functionality needed ~~
def validate_location(value):
    if not value[0].isdigit():
        raise forms.ValidationError("Please enter a valid address.")


# Errand entry form
# ~~ validators still need work ~~
class ErrandForm(forms.ModelForm):
    title = forms.CharField(
        max_length=20,
        strip=True,
        label="Title",
        widget=forms.TextInput(attrs={"placeholder": "shopping"}),
    )
    priority = forms.IntegerField(
        label="Priority",
        widget=forms.TextInput(attrs={"placeholder": "0 is highest priority"}),
        validators=[],
    )
    streetaddr = forms.CharField(
        max_length=20,
        strip=True,
        label="Street Address",
        widget=forms.TextInput(attrs={"placeholder": "123 Sesame Street"}),
        validators=[validators.MinLengthValidator(6)],
    )
    city = forms.CharField(
        max_length=20,
        strip=True,
        label="City",
        widget=forms.TextInput(attrs={"placeholder": "Sunnyville"}),
        validators=[validators.MinLengthValidator(3)],
    )
    state = forms.CharField(
        max_length=2,
        strip=True,
        label="State",
        widget=forms.TextInput(attrs={"placeholder": "CA"}),
        validators=[validators.MaxLengthValidator(2)],
    )
    zip = forms.IntegerField(
        label="Zip Code",
        widget=forms.TextInput(attrs={"placeholder": "85358"}),
        validators=[],
    )
    duration = forms.IntegerField(
        label="Duration Est.",
        widget=forms.TextInput(attrs={"placeholder": ""}),
        validators=[],
    )  # this needs to change depending on how date/time are handled

    class Meta:
        model = Event
        fields = ("title", "priority", "streetaddr", "city", "state", "zip", "duration")


class EventForm(forms.ModelForm):
    title = forms.CharField(
        max_length=20,
        strip=True,
        label="Title",
        widget=forms.TextInput(attrs={"placeholder": "Class"}),
    )
    streetaddr = forms.CharField(
        max_length=20,
        strip=True,
        label="Street Address",
        widget=forms.TextInput(attrs={"placeholder": "1234 Sesame Street"}),
        validators=[validators.MinLengthValidator(6)],
    )
    city = forms.CharField(
        max_length=20,
        strip=True,
        label="City",
        widget=forms.TextInput(attrs={"placeholder": "Sunnyville"}),
        validators=[validators.MinLengthValidator(3)],
    )
    state = forms.CharField(
        max_length=2,
        strip=True,
        label="State",
        widget=forms.TextInput(attrs={"placeholder": "CA"}),
        validators=[validators.MaxLengthValidator(2)],
    )
    zip = forms.IntegerField(
        label="Zip Code",
        widget=forms.TextInput(attrs={"placeholder": "85358"}),
        validators=[],
    )
    start = forms.DateTimeField(
        label="Start",
        widget=forms.DateTimeInput(attrs={"placeholder": "m/d/y H:M"}),
        validators=[],
    )  # this needs to change depending on how date/time are handled
    duration = forms.IntegerField(
        label="Duration", validators=[]
    )  # this needs to change depending on how date/time are handled

    class Meta:
        model = Event
        fields = ("title", "streetaddr", "city", "state", "zip", "start", "duration")
