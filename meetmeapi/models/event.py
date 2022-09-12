from django.db import models

class Event(models.Model):

    name = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    date = models.DateField()
    time = models.TimeField()
    organizer = models.ForeignKey("MeetMeUser", on_delete=models.CASCADE)
    attendees = models.ManyToManyField("MeetMeUser", through="EventUser", related_name="attending")
    description = models.CharField(max_length=1000)
    coordinates = models.JSONField()

    @property
    def joined(self):
        return self.__joined

    @joined.setter
    def joined(self, value):
        self.__joined = value