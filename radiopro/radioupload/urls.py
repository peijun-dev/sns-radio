from django.urls import path
from django.conf.urls import url,include
 
from . import views
 
# set the application namespace
# https://docs.djangoproject.com/en/2.0/intro/tutorial03/
app_name = 'radioupload'

urlpatterns = [
    path('', views.form, name='upload'),
    url(r'^complete/', views.complete, name = 'complete'),
]