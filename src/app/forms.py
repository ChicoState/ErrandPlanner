from django import forms
from django.core import validators
from django.contrib.auth.models import User
from app.models import Event


# Errand entry form
# ~~ validators still need work ~~
class ErrandForm(forms.ModelForm):
    title = forms.CharField(
        max_length=20,
        strip=True,
        label="Title",
        widget=forms.TextInput(attrs={"placeholder": "Grocery Shop"}),
        validators=[validators.RegexValidator(regex=".*[a-zA-Z]+.*")],
    )
    priority = forms.IntegerField(
        label="Priority",
        widget=forms.TextInput(attrs={"placeholder": "1"}),
        validators=[validators.RegexValidator(regex="\d{1,}")],
    )
    streetaddr = forms.CharField(
        max_length=20,
        strip=True,
        label="Street Address",
        widget=forms.TextInput(attrs={"placeholder": "1234 Sesame Street"}),
        validators=[
            validators.MinLengthValidator(6),
            validators.RegexValidator(regex="[0-9]{1,5}[a-zA-Z]*"),
        ],
    )
    city = forms.CharField(
        max_length=20,
        strip=True,
        label="City",
        widget=forms.TextInput(attrs={"placeholder": "Sunnyville"}),
        validators=[
            validators.MinLengthValidator(3),
            validators.RegexValidator(regex="[a-zA-Z]{1,20}"),
        ],
    )
    state = forms.CharField(
        max_length=2,
        strip=True,
        label="State",
        widget=forms.TextInput(attrs={"placeholder": "CA"}),
        validators=[
            validators.MaxLengthValidator(2),
            validators.RegexValidator(regex="[a-zA-Z]{2}"),
        ],
    )
    zip = forms.IntegerField(
        label="Zip Code",
        widget=forms.TextInput(attrs={"placeholder": "85358"}),
        validators=[validators.RegexValidator(regex="[0-9]*")],
    )
    duration = forms.IntegerField(
        label="Duration Est.",
        widget=forms.TextInput(attrs={"placeholder": ""}),
        validators=[validators.RegexValidator(regex="\d{1,}")],
    )  # this needs to change depending on how date/time are handled
    deadline = forms.DateTimeField(
        label="Deadline",
        widget=forms.TextInput(attrs={"placeholder": "10/31/2023 13:15:00"}),
        required=False,
    )

    class Meta:
        model = Event
        fields = (
            "title",
            "priority",
            "streetaddr",
            "city",
            "state",
            "zip",
            "duration",
            "deadline",
        )


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
