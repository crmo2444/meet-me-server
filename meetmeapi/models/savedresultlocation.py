from distutils.archive_util import make_zipfile
from django.db import models

class SavedResultLocation(models.Model):

    user = models.ForeignKey("MeetMeUser", on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    coordinate = models.JSONField()
    address = models.CharField(max_length=500)
    distance = models.FloatField()
    created_on = models.DateField()
