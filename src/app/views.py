from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from datetime import datetime, timedelta
from . import models
from app.forms import JoinForm, LoginForm, ErrandForm, EventForm
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.


def join(request):
    if request.method == "POST":
        join_form = JoinForm(request.POST)
        if join_form.is_valid():
            user = join_form.save()  # Save form data to DB
            user.set_password(user.password)  # Encrypt the password
            user.save()  # Save encrypted password to DB
            # Success! Redirect to home page.
            return redirect("/")
        else:
            # Form invalid, print errors to console
            context = {"join_form": join_form}
            return render(request, "join.html", context)
    else:
        join_form = JoinForm()
        context = {"join_form": join_form}
        return render(request, "join.html", context)


def user_login(request):
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            # First get the username and password supplied
            username = login_form.cleaned_data["username"]
            password = login_form.cleaned_data["password"]
            # Django's built-in authentication function:
            user = authenticate(username=username, password=password)
            # If we have a user
            if user:
                # Check if the account is active
                if user.is_active:
                    login(request, user)  # Log the user in.
                    # Send the user back to homepage
                    return redirect("/")
            else:
                # If account is not active:
                return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(
                username, password))
            return render(request, "login.html", {"login_form": LoginForm})
    else:
        # Nothing has been provided for username or password.
        return render(request, "login.html", {"login_form": LoginForm})


## Calendar Views ##


@login_required()
def addEvent(request):
    if request.method == "POST":
        if "add" in request.POST:
            # User has added an errand
            add_form = EventForm(request.POST)
            if add_form.is_valid():
                title = add_form.cleaned_data["title"]
                streetaddr = add_form.cleaned_data["streetaddr"]
                city = add_form.cleaned_data["city"]
                state = add_form.cleaned_data["state"]
                zip = add_form.cleaned_data["zip"]
                start = add_form.cleaned_data["start"]
                duration = add_form.cleaned_data["duration"]
                user = User.objects.get(id=request.user.id)
                models.Event(
                    user=user,
                    title=title,
                    priority=-1,
                    streetaddr=streetaddr,
                    city=city,
                    state=state,
                    zip=zip,
                    start=start,
                    duration=duration,
                ).save()
                return redirect("/calendar/")
            else:
                context = {"form_data": add_form}
                return render(request, "addEvent.html", context)
        else:
            # Cancel
            return redirect("/calendar/")
    else:
        context = {"form_data": EventForm()}
        return render(request, "addEvent.html", context)


class Date:
    day = ""
    date = (
        datetime.now()
    )  # default to right now as a time field. this will be updated before display
    events = []  # holds the day's events


@login_required()
def calendar(request):
    # get today
    today = datetime.today()
    todaydate = today.weekday()  # gets today's date 0-6 mon-sun
    todaydate = todaydate + 1 if todaydate < 6 else 0

    # get the first day in the week
    sunday = Date()
    sunday.date = today - timedelta(days=todaydate)
    sunday.day = "Sunday"
    sunday.date = sunday.date.replace(hour=0, minute=0, second=0)

    # use the first day to get the other days in the week
    monday = Date()
    tuesday = Date()
    wednesday = Date()
    thursday = Date()
    friday = Date()
    saturday = Date()
    monday.date = monday.date + timedelta(days=1)
    monday.day = "Monday"
    tuesday.date = monday.date + timedelta(days=2)
    tuesday.day = "Tuesday"
    wednesday.date = monday.date + timedelta(days=3)
    wednesday.day = "Wednesday"
    thursday.date = monday.date + timedelta(days=4)
    thursday.day = "Thursday"
    friday.date = monday.date + timedelta(days=5)
    friday.day = "Friday"
    saturday.date = monday.date + timedelta(days=6)
    saturday.day = "Saturday"

    # get all of the events that would be in the current week

    sunday.events = models.Event.objects.filter(
        user=request.user, start__range=(sunday.date, (monday.date))
    )
    monday.events = models.Event.objects.filter(
        user=request.user, start__range=(monday.date, (tuesday.date))
    )
    tuesday.events = models.Event.objects.filter(
        user=request.user, start__range=(tuesday.date, (wednesday.date))
    )
    wednesday.events = models.Event.objects.filter(
        user=request.user, start__range=(wednesday.date, (thursday.date))
    )
    thursday.events = models.Event.objects.filter(
        user=request.user, start__range=(thursday.date, (friday.date))
    )
    friday.events = models.Event.objects.filter(
        user=request.user, start__range=(friday.date, (saturday.date))
    )
    saturday.events = models.Event.objects.filter(
        user=request.user,
        start__range=(saturday.date, (sunday.date + timedelta(days=7))),
    )

    # place each day into the schedule
    schedule = [sunday, monday, tuesday, wednesday, thursday, friday, saturday]

    context = {
        "schedule": schedule,
    }
    return render(request, "calendar.html", context)


## Errand Views ##


@login_required()
def errands(request):
    table_data = models.Event.objects.filter(is_errand=True, user=request.user)
    context = {"table_data": table_data}
    return render(request, "errands.html", context)

# Add errand
@login_required()
def addErrand(request):
    if request.method == "POST":
        if "add" in request.POST:
            # User has added an errand
            add_form = ErrandForm(request.POST)
            if add_form.is_valid():
                title = add_form.cleaned_data["title"]
                priority = add_form.cleaned_data["priority"]
                streetaddr = add_form.cleaned_data["streetaddr"]
                city = add_form.cleaned_data["city"]
                state = add_form.cleaned_data["state"]
                zip = add_form.cleaned_data["zip"]
                duration = add_form.cleaned_data["duration"]
                user = User.objects.get(id=request.user.id)
                models.Event(
                    user=user,
                    title=title,
                    priority=priority,
                    streetaddr=streetaddr,
                    city=city,
                    state=state,
                    zip=zip,
                    duration=duration,
                    is_errand=True,
                    scheduled=False,
                ).save()
                return redirect("/errands/")
            else:
                context = {"form_data": add_form}
                return render(request, "addErrand.html", context)
        else:
            # Cancel
            return redirect("/errands/")
    else:
        context = {"form_data": ErrandForm()}
    return render(request, "addErrand.html", context)


# Edit errand
@login_required(login_url="/login/")
def editErrand(request, id):
    if request.method == "GET":
        # Load Errand Entry Form with current model data.
        errand = models.Event.objects.get(id=id)
        form = ErrandForm(instance=errand)
        context = {"form_data": form}
        return render(request, "editErrand.html", context)
    elif request.method == "POST":
        # Process form submission
        if "edit" in request.POST:
            form = ErrandForm(request.POST)
            if form.is_valid():
                errand = form.save(commit=False)
                errand.user = request.user
                errand.id = id
                errand.save()
                return redirect("/errands/")
            else:
                context = {"form_data": form}
                return render(request, "addErrand.html", context)
        else:
            # Cancel
            return redirect("/errands/")


# This the the function to delete the errand
@login_required()
def delete_errand(request, pk):
    prod = models.Event.objects.get(id=pk)
    prod.delete()
    messages.success(request, "errand deleted successfully")
    return redirect('/errands')
