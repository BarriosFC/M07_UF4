from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader

# Create your views here.

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def students(request):
    alumnos = [
        {"id":"1","name":"Kevin","surname":"Arata","email":"kevin@itic.com","role":"student","modules":"Cuenta la leyenda que este muchacho existe"},
        {"id":"2","name":"Larry","surname":"Medino","email":"larry@itic.com","role":"student","modules":"Ninguno"},
        {"id":"3","name":"Joana Jiayun","surname":"Lin Chen","email":"joana@itic.com","role":"student","modules":"M06, M07, M08, M09, Híbridas"},
        {"id":"4","name":"Oscar","surname":"Perez Mengual","email":"oscarin@itic.com","role":"student","modules":"M06, M07, M08, M09, Híbridas"},
        {"id":"5","name":"Eric","surname":"Sanchez Vazquez","email":"eric@itic.com","role":"student","modules":"M06, M07, M08, M09, Híbridas"},
        {"id":"6","name":"Junhong","surname":"Zhu Zhang","email":"junhong@itic.com","role":"student","modules":"M06, M07, M08, M09, Híbridas"},
        {"id":"7","name":"Alexander","surname":"Andreev Apukhtina","email":"alexander@itic.com","role":"student","modules":"M06, M07, M08, M09, Híbridas"},
        {"id":"8","name":"Anxo","surname":"Aragundi Mesias","email":"anxo@itic.com","role":"student","modules":"M06, M07, M08, M09, Híbridas"},
        {"id":"9","name":"Adria","surname":"Garcia Perez","email":"adria@itic.com","role":"student","modules":"M06, M07, M08, M09, Híbridas"},
        {"id":"10","name":"Carlos Andres","surname":"Zambrano Aray","email":"andres@itic.com","role":"student","modules":"M06, M07, M08, M09, Híbridas"},
        {"id":"11","name":"Facundo 'The King'","surname":"Barrios","email":"theking@itic.com","role":"student","modules":"M06, M07, M08, M09, Híbridas"},
        {"id":"12","name":"Joel","surname":"Ghanem Gomez","email":"joel@itic.com","role":"student","modules":"M06, M07, M08, M09, Híbridas"},
        {"id":"13","name":"Angelo","surname":"Montenegro Zavala","email":"angeluz@itic.com","role":"student","modules":"M06, M07, M08, M09, Híbridas"},
        {"id":"14","name":"Oriana Saray","surname":"Rojas Guedez","email":"oriana@itic.com","role":"student","modules":"M06, M07, M08, M09, Híbridas"},
        {"id":"15","name":"Neus","surname":"Bravo Arias","email":"neus@itic.com","role":"student","modules":"M06, M07, M08, M09, Híbridas"},
        {"id":"16","name":"Angel","surname":"Ivanov Spasov","email":"angel@itic.com","role":"student","modules":"M06, M07, M08, M09, Híbridas"},
        {"id":"17","name":"Dinar","surname":"Khazimullin","email":"dinar@itic.com","role":"student","modules":"M06, M07, M08, M09, Híbridas"},
        {"id":"18","name":"Jesus","surname":"Pujada Montoya","email":"yisuscraist@itic.com","role":"student","modules":"M06, M07, M08, M09"},
        {"id":"19","name":"Veronica","surname":"Cartagena Jaldin","email":"veronica@itic.com","role":"student","modules":"M06, M07, M08, M09, Híbridas"},
        {"id":"20","name":"Gemma","surname":"Garrigosa Frances","email":"gemma@itic.com","role":"student","modules":"M06, M07, M08, M09, Híbridas"},
    ]
    context = {'users': alumnos, 'role': 'Alumnos'}
    return render(request, 'table.html', context )

def teachers(request):
    profesores = [
        {"id":"21","name":"Juan Manuel","surname":"Sanchez","email":"juanma@itic.com","role":"teacher","modules":"M06"},
        {"id":"22","name":"Roger","surname":"Sobrino","email":"roger@itic.com","role":"teacher","modules":"M07"},
        {"id":"23","name":"Xavi","surname":"Quesada","email":"xavi@itic.com","role":"teacher","modules":"M08, Híbridas"},
        {"id":"24","name":"Oriol","surname":"Roca","email":"oriol@itic.com","role":"teacher","modules":"M09"},
    ]
    context = {'users': profesores, 'role': 'Profesores'}
    #objeto context
    return render(request, 'table.html', context )

def user(request, id):
    users = [
        {"id":"1","name":"Kevin","surname":"Arata","email":"kevin@itic.com","role":"student","modules":"Cuenta la leyenda que este muchacho existe"},
        {"id":"2","name":"Larry","surname":"Medino","email":"larry@itic.com","role":"student","modules":"Ninguno"},
        {"id":"3","name":"Joana Jiayun","surname":"Lin Chen","email":"joana@itic.com","role":"student","modules":"M06, M07, M08, M09, Híbridas"},
        {"id":"4","name":"Oscar","surname":"Perez Mengual","email":"oscarin@itic.com","role":"student","modules":"M06, M07, M08, M09, Híbridas"},
        {"id":"5","name":"Eric","surname":"Sanchez Vazquez","email":"eric@itic.com","role":"student","modules":"M06, M07, M08, M09, Híbridas"},
        {"id":"6","name":"Junhong","surname":"Zhu Zhang","email":"junhong@itic.com","role":"student","modules":"M06, M07, M08, M09, Híbridas"},
        {"id":"7","name":"Alexander","surname":"Andreev Apukhtina","email":"alexander@itic.com","role":"student","modules":"M06, M07, M08, M09, Híbridas"},
        {"id":"8","name":"Anxo","surname":"Aragundi Mesias","email":"anxo@itic.com","role":"student","modules":"M06, M07, M08, M09, Híbridas"},
        {"id":"9","name":"Adria","surname":"Garcia Perez","email":"adria@itic.com","role":"student","modules":"M06, M07, M08, M09, Híbridas"},
        {"id":"10","name":"Carlos Andres","surname":"Zambrano Aray","email":"andres@itic.com","role":"student","modules":"M06, M07, M08, M09, Híbridas"},
        {"id":"11","name":"Facundo 'The King'","surname":"Barrios","email":"theking@itic.com","role":"student","modules":"M06, M07, M08, M09, Híbridas"},
        {"id":"12","name":"Joel","surname":"Ghanem Gomez","email":"joel@itic.com","role":"student","modules":"M06, M07, M08, M09, Híbridas"},
        {"id":"13","name":"Angelo","surname":"Montenegro Zavala","email":"angeluz@itic.com","role":"student","modules":"M06, M07, M08, M09, Híbridas"},
        {"id":"14","name":"Oriana Saray","surname":"Rojas Guedez","email":"oriana@itic.com","role":"student","modules":"M06, M07, M08, M09, Híbridas"},
        {"id":"15","name":"Neus","surname":"Bravo Arias","email":"neus@itic.com","role":"student","modules":"M06, M07, M08, M09, Híbridas"},
        {"id":"16","name":"Angel","surname":"Ivanov Spasov","email":"angel@itic.com","role":"student","modules":"M06, M07, M08, M09, Híbridas"},
        {"id":"17","name":"Dinar","surname":"Khazimullin","email":"dinar@itic.com","role":"student","modules":"M06, M07, M08, M09, Híbridas"},
        {"id":"18","name":"Jesus","surname":"Pujada Montoya","email":"yisuscraist@itic.com","role":"student","modules":"M06, M07, M08, M09"},
        {"id":"19","name":"Veronica","surname":"Cartagena Jaldin","email":"veronica@itic.com","role":"student","modules":"M06, M07, M08, M09, Híbridas"},
        {"id":"20","name":"Gemma","surname":"Garrigosa Frances","email":"gemma@itic.com","role":"student","modules":"M06, M07, M08, M09, Híbridas"},       
        {"id":"21","name":"Juan Manuel","surname":"Sanchez","email":"juanma@itic.com","role":"teacher","modules":"M06"},
        {"id":"22","name":"Roger","surname":"Sobrino","email":"roger@itic.com","role":"teacher","modules":"M07"},
        {"id":"23","name":"Xavi","surname":"Quesada","email":"xavi@itic.com","role":"teacher","modules":"M08, Híbridas"},
        {"id":"24","name":"Oriol","surname":"Roca","email":"oriol@itic.com","role":"teacher","modules":"M09"},
    ]

    user = {"id":"99","name":"Undefined","surname":"Undefined","email":"Undefined","role":"Undefined","modules":"Undefined"},

    for usuario in users:
        if usuario["id"] == id:
            user = usuario
    
    context = {'user': user}
    return render(request, 'user.html', context)