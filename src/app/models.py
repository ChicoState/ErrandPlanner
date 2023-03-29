from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Errand model
class Errand(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.SmallIntegerField(primary_key=True)
    title = models.CharField(max_length=20)
    priority = models.SmallIntegerField()
    # address fields
    streetaddr = models.CharField(max_length=30)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=2)
    zip = models.SmallIntegerField() # more for last 4?
    # time variables 
    # can be left blank (alternatively we could assign a default value)
    start = models.DateTimeField(blank=True)
    end = models.DateTimeField(blank=True)
    duration = models.DurationField(blank=True) 
    class Meta:
        unique_together = ("user", "id")
