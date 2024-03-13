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
        {"name":"Larry","surname":"Medino","email":"larry@itic.com"},
        {"name":"Joana Jiayun","surname":"Lin Chen","email":"joana@itic.com"},
        {"name":"Oscar","surname":"Perez Mengual","email":"oscarin@itic.com"},
        {"name":"Eric","surname":"Sanchez Vazquez","email":"eric@itic.com"},
        {"name":"Junhong","surname":"Zhu Zhang","email":"junhong@itic.com"},
        {"name":"Alexander","surname":"Andreev Apukhtina","email":"alexander@itic.com"},
        {"name":"Anxo","surname":"Aragundi Mesias","email":"anxo@itic.com"},
        {"name":"Adria","surname":"Garcia Perez","email":"adria@itic.com"},
        {"name":"Carlos Andres","surname":"Zambrano Aray","email":"andres@itic.com"},
        {"name":"Facundo 'The King'","surname":"Barrios","email":"theking@itic.com"},
        {"name":"Joel","surname":"Ghanem Gomez","email":"joel@itic.com"},
        {"name":"Angelo","surname":"Montenegro Zavala","email":"angeluz@itic.com"},
        {"name":"Oriana Saray","surname":"Rojas Guedez","email":"oriana@itic.com"},
        {"name":"Neus","surname":"Bravo Arias","email":"neus@itic.com"},
        {"name":"Angel","surname":"Ivanov Spasov","email":"angel@itic.com"},
        {"name":"Dinar","surname":"Khazimullin","email":"dinar@itic.com"},
        {"name":"Jesus","surname":"Pujada Montoya","email":"yisuscraist@itic.com"},
        {"name":"Veronica","surname":"Cartagena Jaldin","email":"veronica@itic.com"},
        {"name":"Gemma","surname":"Garrigosa Frances","email":"gemma@itic.com"},
    ]
    context = {'users': alumnos, 'role': 'Alumnos'}
    return render(request, 'table.html', context )

def teachers(request):
    profesores = [
        {"name":"Juan Manuel","surname":"Sanchez","module":"M06"},
        {"name":"Roger","surname":"Sobrino","module":"M07"},
        {"name":"Xavi","surname":"Quesada","module":"M08"},
        {"name":"Oriol","surname":"Roca","module":"M09"},
    ]
    context = {'users': profesores, 'role': 'Profesores'}
    #objeto context
    return render(request, 'table.html', context )