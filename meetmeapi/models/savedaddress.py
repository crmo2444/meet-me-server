from distutils.archive_util import make_zipfile
from django.db import models

class SavedAddress(models.Model):

    user = models.ForeignKey("MeetMeUser", on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=500)
    coordinates = models.JSONField()
