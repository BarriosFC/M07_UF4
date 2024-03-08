from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def students(request):
    return HttpResponse("Desde Alumnos")

def teachers(request):
    return HttpResponse("Desde Profes")