from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader

# Create your views here.

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def students(request):
    alumnos = [
        {"id":"1","name":"Kevin","surname":"Arata","email":"kevin@itic.com"},
        {"id":"2","name":"Larry","surname":"Medino","email":"larry@itic.com"},
        {"id":"3","name":"Joana Jiayun","surname":"Lin Chen","email":"joana@itic.com"},
        {"id":"4","name":"Oscar","surname":"Perez Mengual","email":"oscarin@itic.com"},
        {"id":"5","name":"Eric","surname":"Sanchez Vazquez","email":"eric@itic.com"},
        {"id":"6","name":"Junhong","surname":"Zhu Zhang","email":"junhong@itic.com"},
        {"id":"7","name":"Alexander","surname":"Andreev Apukhtina","email":"alexander@itic.com"},
        {"id":"8","name":"Anxo","surname":"Aragundi Mesias","email":"anxo@itic.com"},
        {"id":"9","name":"Adria","surname":"Garcia Perez","email":"adria@itic.com"},
        {"id":"10","name":"Carlos Andres","surname":"Zambrano Aray","email":"andres@itic.com"},
        {"id":"11","name":"Facundo 'The King'","surname":"Barrios","email":"theking@itic.com"},
        {"id":"12","name":"Joel","surname":"Ghanem Gomez","email":"joel@itic.com"},
        {"id":"13","name":"Angelo","surname":"Montenegro Zavala","email":"angeluz@itic.com"},
        {"id":"14","name":"Oriana Saray","surname":"Rojas Guedez","email":"oriana@itic.com"},
        {"id":"15","name":"Neus","surname":"Bravo Arias","email":"neus@itic.com"},
        {"id":"16","name":"Angel","surname":"Ivanov Spasov","email":"angel@itic.com"},
        {"id":"17","name":"Dinar","surname":"Khazimullin","email":"dinar@itic.com"},
        {"id":"18","name":"Jesus","surname":"Pujada Montoya","email":"yisuscraist@itic.com"},
        {"id":"19","name":"Veronica","surname":"Cartagena Jaldin","email":"veronica@itic.com"},
        {"id":"20","name":"Gemma","surname":"Garrigosa Frances","email":"gemma@itic.com"},
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

def user(request, id):
    # de momento voy a hardcodear un usuario y siempre se mostrará el mismo
    # pero a partir de la práctica 2 podré hacer consultas y cambiaré el método
    user = {
        "id":id,
        "name":"Persona",
        "surname":"Genérica",
        "email":"email@email.com",
        "role":"Ciudadano de bien",
        "modules":"M06, M07, M08, M09, Híbridas",
    }
    context = {'user': user}
    return render(request, 'user.html', context)