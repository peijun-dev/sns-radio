from django import forms
from radioupload.models import FileModel


class FileForm(forms.ModelForm):
    class Meta:
        model = FileModel
        fields = ('title', 'description', 'thumbnail', 'file',)