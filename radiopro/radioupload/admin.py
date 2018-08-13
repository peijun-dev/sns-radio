from django.contrib import admin

# Register your models here.

from radioupload.models import FileModel

class FileAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'uploaded_at')
    list_display_link = ('id')

admin.site.register(FileModel, FileAdmin)
