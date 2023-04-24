from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from datetime import datetime, timedelta
from . import models
from app.forms import ErrandForm, EventForm
from django.contrib.auth.models import User
from django.contrib import messages
from authlib.integrations.django_client import OAuth
from functools import wraps

# Create your views here.

CONF_URL = "https://accounts.google.com/.well-known/openid-configuration"
oauth = OAuth()
oauth.register(
    name="google",
    server_metadata_url=CONF_URL,
    client_kwargs={"scope": "openid email profile"},
)


# Function decorator that checks whether there is an active user
def auth_required(func):
    @wraps(func)
    def wrapper(request):
        user = request.session.get("user")
        if user:
            return func(request)
        else:
            return redirect("/login")

    return wrapper


def login(request):
    redirect_uri = "http://127.0.0.1:8000/auth/"  # TODO: Change URL to match what works
    return oauth.google.authorize_redirect(request, redirect_uri)


def logout(request):
    request.session.flush()
    return redirect("/")


def auth(request):
    token = oauth.google.authorize_access_token(request)
    request.session["user"] = token["userinfo"]
    print(request.session.get("user"))
    return redirect("/")


## Errand Views ##


@auth_required
def errands(request):
    # Simply load errands for rendering
    email = request.session.get("user")["email"]
    table_data = models.Event.objects.filter(user=email)
    context = {"table_data": table_data}
    return render(request, "errands.html", context)


@auth_required
def delete_errand(request, pk):
    prod = models.Event.objects.get(id=pk)
    prod.delete()
    messages.success(request, "errand deleted successfully")
    return redirect("/errands")


# Add errand
@auth_required
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
                user = request.session.get("user")["email"]
                models.Event(
                    user=user,
                    title=title,
                    priority=priority,
                    streetaddr=streetaddr,
                    city=city,
                    state=state,
                    zip=zip,
                    duration=duration,
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


@auth_required
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
                errand.scheduled = False
                errand.save()
                return redirect("/errands/")
            else:
                context = {"form_data": form}
                return render(request, "addErrand.html", context)
        else:
            # Cancel
            return redirect("/errands/")
