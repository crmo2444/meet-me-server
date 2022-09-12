from django.db import models

class EventUser(models.Model):

    user = models.ForeignKey("MeetMeUser", on_delete=models.CASCADE)
    event = models.ForeignKey("Event", on_delete=models.CASCADE)