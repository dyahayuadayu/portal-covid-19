from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.serializers import serialize
from django.http import HttpResponse
from . models import Counties,Incidences
# Create your views here.

def county_datasets(request):
    try:
        # Your code that may throw an exception
        counties = serialize('geojson', Counties.objects.all())
        return HttpResponse(counties,content_type='json')
    except Exception as e:
        print (str(e))
        return HttpResponse("<h1>no data</h1>")

    

def point_datasets(request):
    points = serialize('geojson', Incidences.objects.all())
    return HttpResponse(points,content_type='json')