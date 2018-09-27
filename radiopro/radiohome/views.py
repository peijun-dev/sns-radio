from django.shortcuts import render
from django.http import HttpResponse
from radioupload.models import FileModel

# Create your views here.

def index(request):
    data = FileModel.objects.all()
    params = {
        'data' : data,
    }
    return render(request, 'radiohome/index.html', params)
