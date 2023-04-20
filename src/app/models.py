from django.db import models
from django.contrib.auth.models import User


# Event model
class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # id = models.SmallIntegerField(primary_key=True)
    title = models.CharField(max_length=20)
    priority = models.SmallIntegerField()
    # address fields
    streetaddr = models.CharField(max_length=30)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=2)
    zip = models.SmallIntegerField()  # more for last 4?
    # time variables
    # can be left blank (alternatively we could assign a default value)
    start = models.DateTimeField(blank=True, null=True)
    duration = models.IntegerField(blank=True)
    deadline = models.DateTimeField(blank=True, null=True)
    # Used to determine if a modell is an errand or a regular event
    is_errand = models.BooleanField(default=False)
    scheduled = models.BooleanField(default=True)

    def __str__(self):
        strRep = (
            ("Errand: " if self.is_errand else "Event: ")
            + self.title
            + " ("
            + self.user.username
            + ")"
        )
        return strRep

    class Meta:
        unique_together = ("user", "id")
