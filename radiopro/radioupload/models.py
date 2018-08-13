from django.db import models

# Create your models here.

from datetime import datetime


class FileModel(models.Model):
    file = models.FileField(upload_to='radiofile/')
    title = models.CharField(max_length=32, blank=False)
    description = models.CharField(max_length=255, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
