from django.db import models

# Create your models here.

from datetime import datetime

class FileNameModel(models.Model):
    file_name = models.CharField(max_length = 50)
    upload_time = models.DateTimeField(default = datetime.now)

    def __str__(self):
        return self.title
 
    def get_filename(self):
        return os.path.basename(self.file_name)
