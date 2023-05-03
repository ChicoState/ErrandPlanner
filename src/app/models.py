from django.db import models


# Event model
class Event(models.Model):
    user = models.EmailField()
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
    scheduled = models.BooleanField(default=True)
    is_completed = models.BooleanField(default=False)
    time_completed = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        strRep = self.title + " (" + self.user + ")"
        return strRep

    class Meta:
        unique_together = ("user", "id")
