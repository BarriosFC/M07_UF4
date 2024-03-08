from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader

# Create your views here.

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def students(request):
    alumnos = [
        {"name":"Kevin","surname":"Arata","email":"kevin@itic.com"},
        {"name":"Facundo","surname":"Barrios","email":"facundo@itic.com"},
        {"name":"Angelo","surname":"Montenegro","email":"angelo@itic.com"},
        {"name":"Neus","surname":"Bravo","email":"neus@itic.com"},
        {"name":"Adrià","surname":"Garcçia","email":"adria@itic.com"},
        {"name":"Gemma","surname":"Garrigosa","email":"gemma@itic.com"},
        {"name":"Oscar","surname":"Perez","email":"oscar@itic.com"},
        {"name":"Larry","surname":"Medino","email":"larry@itic.com"},
        {"name":"Kevin again","surname":"Arata","email":"kevin2@itic.com"},
    ]
    context = {'alumnos': alumnos}
    return render(request, 's_index.html', context )

def teachers(request):
    profesores = [
        {"name":"Juan Manuel","surname":"Sanchez","module":"M06"},
        {"name":"Roger","surname":"Sobrino","module":"M07"},
        {"name":"Xavi","surname":"Quesada","module":"M08"},
        {"name":"Oriol","surname":"Roca","module":"M09"},
    ]
    context = {'profes': profesores}
    #objeto context
    return render(request, 't_index.html', context )