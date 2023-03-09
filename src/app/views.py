<<<<<<< HEAD
from django.contrib.auth import authenticate, login, logout 
from django.http import HttpResponseRedirect, HttpResponse 
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from app.forms import JoinForm , LoginForm

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
                
=======
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from datetime import timedelta

# Create your views here.

class Date:
    start = datetime.now() #default to right now as a time field. this will be updated before display
    events = [] #holds the day's events

def calendar(request):
    #get today
    today = datetime.today()
    todaydate = today.weekday()

    #get the first day in the week
    monday = Date
    monday.start = today - timedelta(days = todaydate)
    
    #use the first day to get the other days in the week
    tuesday = Date
    wednesday = Date
    thursday = Date
    friday = Date
    saturday = Date
    sunday = Date
    sunday.start = monday.start - timedelta(days = 1)
    tuesday.start = monday.start + timedelta(days = 1)
    wednesday.start = monday.start + timedelta(days = 2)
    thursday.start = monday.start + timedelta(days = 3)
    friday.start = monday.start + timedelta(days = 4)
    saturday.start = monday.start + timedelta(days = 5)

    #get all of the events that would be in the current week

    #fiter the events for only the ones that would appear on the current week: 
    # if they end before the start of the week or start after the week is over, they are not selected
    week = Events.all.filter( End > sunday.start )
    weekevents = week.filter( Start < ( saturday.start + timedelta(days=1)))

    #place each event into a day, depending 
    for e in weekevents:
        #check sunday
        if(e.start > sunday.start and e.start < monday.start):
            sunday.events.append(e)
        #check monday
        if(e.start > monday.start and e.start < tuesday.start):
            monday.events.append(e)
        #check tuesday
        if(e.start > tuesday.start and e.start < wednesday.start):
            tuesday.events.append(e)
        #check wednesday
        if(e.start > wednesday.start and e.start < thursday.start):
            wednesday.events.append(e)
        #check thursday
        if(e.start > thursday.start and e.start < friday.start):
            thursday.events.append(e)
        #check friday
        if(e.start > friday.start and e.start < saturday.start):
            friday.events.append(e)
        #check saturday
        if(e.start > saturday.start and e.start < (saturday.start + timedelta(days=1))):
            saturday.events.append(e)

    #place each day into the schedule
    schedule = [ sunday, monday, tuesday, wednesday, thursday, friday, saturday ]
    
    context = {
        schedule:schedule,

    }
    return HttpResponse('bootstrap.html', context)
>>>>>>> calendarBackend
