from django.db import models

##Create your models here.

##Day: contains the details of what the calendar needs to operate
class Event:
    Start = models.DateTimeField()
    End = models.DateTimeField()
    Name = models.CharField(max_length=50)
    ##Place = models.
