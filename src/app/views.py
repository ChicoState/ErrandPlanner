from django.contrib.auth import authenticate, login, logout 
from django.http import HttpResponseRedirect, HttpResponse 
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from app.forms import JoinForm , LoginForm
from datetime import datetime, timedelta
from . import models

# Create your views here.

def join(request):
    if (request.method == "POST"):
        join_form = JoinForm(request.POST)
        if (join_form.is_valid()):
            # Save form data to DB
            user = join_form.save()
            # Encrypt the password
            user.set_password(user.password)
            # Save encrypted password to DB 
            user.save()
            # Success! Redirect to home page.
            return redirect("/")
        else:
            # Form invalid, print errors to console
            page_data = { "join_form": join_form }
            return render(request, 'join.html', page_data)
        
    else:
        join_form = JoinForm()
        page_data = { "join_form": join_form }
        return render(request, 'join.html', page_data)
    
    
def user_login(request):
    if (request.method == 'POST'):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
        # First get the username and password supplied
            username = login_form.cleaned_data["username"] 
            password = login_form.cleaned_data["password"]
            # Django's built-in authentication function:
            user = authenticate(username=username, password=password) 
            # If we have a user
            if user:
            #Check it the account is active 
                if user.is_active:
                    # Log the user in.
                    login(request,user)
                    # Send the user back to homepage
                    return redirect("/")
            else:
                # If account is not active:
                return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password)) 
            return render(request, 'login.html', {"login_form": LoginForm})
    else:
    #Nothing has been provided for username or password.
        return render(request, 'login.html', {"login_form": LoginForm}) 

#Calendar Backend
class Date:
    day = ""
    date = datetime.now() #default to right now as a time field. this will be updated before display
    events = [] #holds the day's events

def calendar(request):
    #get today
    today = datetime.today()
    todaydate = today.weekday()

    #get the first day in the week
    monday = Date()
    monday.date = today - timedelta(days = todaydate)
    monday.day = "Monday"
    monday.date = monday.date.replace(hour = 0, minute = 0, second = 0)
    
    #use the first day to get the other days in the week
    tuesday = Date()
    wednesday = Date()
    thursday = Date()
    friday = Date()
    saturday = Date()
    sunday = Date()
    sunday.date = monday.date - timedelta(days = 1)
    sunday.day = "Sunday"
    tuesday.date = monday.date + timedelta(days = 1)
    tuesday.day = "Tuesday"
    wednesday.date = monday.date + timedelta(days = 2)
    wednesday.day = "Wednesday"
    thursday.date = monday.date + timedelta(days = 3)
    thursday.day = "Thursday"
    friday.date = monday.date + timedelta(days = 4)
    friday.day = "Friday"
    saturday.date = monday.date + timedelta(days = 5)
    saturday.day = "Saturday"

    #get all of the events that would be in the current week
    
    sunday.events = models.ErrandModel.objects.filter( end__range=(sunday.date, (monday.date)))
    monday.events = models.ErrandModel.objects.filter( end__range=(monday.date, (tuesday.date)))
    tuesday.events = models.ErrandModel.objects.filter( end__range=(tuesday.date, (wednesday.date)))
    wednesday.events = models.ErrandModel.objects.filter( end__range=(wednesday.date, (thursday.date)))
    thursday.events = models.ErrandModel.objects.filter( end__range=(thursday.date, (friday.date)))
    friday.events = models.ErrandModel.objects.filter( end__range=(friday.date, (saturday.date)))
    saturday.events = models.ErrandModel.objects.filter( end__range=(saturday.date, (sunday.date + timedelta(days = 7))))

    #place each day into the schedule
    schedule = [ sunday, monday, tuesday, wednesday, thursday, friday, saturday ]
    
    context = {
        'schedule':schedule,
    }
    return render(request, "calendar.html", context)
