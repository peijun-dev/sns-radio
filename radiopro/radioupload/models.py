from django.db import models
from django.contrib.auth.models import User

# Create your models here.

from datetime import datetime


class FileModel(models.Model):
    file = models.FileField(upload_to='radiofile/')
    user = models.CharField(max_length=500, null=False)
    title = models.CharField(max_length=32, blank=False)
    description = models.CharField(max_length=255, blank=True)
    thumbnail = models.ImageField(upload_to='radiofile/')
    uploaded_at = models.DateTimeField(auto_now_add=True)