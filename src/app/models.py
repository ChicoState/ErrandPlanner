from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# 
class Errand(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.SmallIntegerField()
    title = models.CharField(max_length=20)
    priority = models.SmallIntegerField(max_length=1)
    # address fields
    streetaddr = models.CharField()
    city = models.CharField()
    state = models.CharField(max_length=2)
    zip = models.CharField(max_length=5) # more for last 4?
    # time variables
    start = models.SmallIntegerField(default=0) # needs to change
    end = models.SmallIntegerField(default=0) # needs to change
    duration = models.SmallIntegerField(default=30) # is this the value we want??
    class Meta:
        unique_together = ("user", "id")
