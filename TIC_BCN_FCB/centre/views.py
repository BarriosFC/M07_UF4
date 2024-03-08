from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader

# Create your views here.

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def students(request):
    return HttpResponse("Desde Alumnos")

def teachers(request):
    profe = {"name":"roger","surname":"sobrino","age":"17"}
    # template = loader.get_template('index.html')
    # dades = template.render()
    return render(request, 'p_index.html', {'nombre':profe['name'],'apellido':profe['surname'],'edad':profe['age']})