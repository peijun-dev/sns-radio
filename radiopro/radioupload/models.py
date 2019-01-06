
from django.db import models
from radiopro  import settings

# Create your models here.

from datetime import datetime


class FileModel(models.Model):

    class Meta:
        db_table = 'radiofile'

    file = models.FileField(upload_to='radiofile/')
    user = models.CharField(max_length=500, null=False)
    title = models.CharField(max_length=32, blank=False)
    description = models.CharField(max_length=255, blank=True)
    thumbnail = models.ImageField(upload_to='radiofile/')
    submitter = models.ForeignKey(settings.AUTH_USER_MODEL, models.PROTECT, blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)