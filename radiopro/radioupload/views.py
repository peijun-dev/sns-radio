from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.template.context_processors import csrf
from django.conf import settings
from radioupload.models import FileModel
from radioupload.forms import FileForm
import sys, os

UPLOADE_DIR = os.path.dirname(os.path.abspath(__file__)) + '/static/files/'


# Create your views here.

@login_required
def upload(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('radioupload/complete')
    else:
        form = FileForm()
    return render(request, 'radioupload/upload.html', {
        'form': form
    })

def complete(request):
    return render(request, 'radioupload/complete.html')
