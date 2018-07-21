from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.template.context_processors import csrf
from django.conf import settings
from radioupload.models import FileNameModel
import sys, os

UPLOADE_DIR = os.path.dirname(os.path.abspath(__file__)) + '/static/files/'


# Create your views here.

@login_required
def form(request):
    if request.method != 'POST':
        c = {}
        c.update(csrf(request))
        return render(request, 'radioupload/upload.html')

    file = request.FILES['file']
    path = os.path.join(UPLOADE_DIR, file.name)
    destination = open(path, 'wb')

    for chunk in file.chunks():
        destination.write(chunk)

    insert_data = FileNameModel(file_name = file.name)
    insert_data.save()

    return redirect('radioupload:complete')

def complete(request):
    return render(request, 'radioupload/complete.html')
