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