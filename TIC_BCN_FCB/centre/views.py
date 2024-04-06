from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import Context, loader
from .forms import UserForm
from .models import User

# Create your views here.

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def students(request):
    alumnos = User.objects.filter(role='student')
    context = {'users': alumnos, 'role': 'Alumnos'}
    return render(request, 'table.html', context )

def teachers(request):
    profesores = User.objects.filter(role='teacher')
    context = {'users': profesores, 'role': 'Profesores'}
    #objeto context
    return render(request, 'table.html', context )

# def user(request, id):
#     users = []

#     user = {"id":"99","name":"Undefined","surname":"Undefined","email":"Undefined","role":"Undefined","modules":"Undefined"},

#     for usuario in users:
#         if usuario["id"] == id:
#             user = usuario
    
#     context = {'user': user}
#     return render(request, 'user.html', context)

def user_form(request):
    form = UserForm()

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            if request.POST.get('role') == 'student':
                return redirect('students')
            else:
                return redirect('teachers')    
            
    context = {'form': form }
    return render(request, 'form.html', context)


def update_user(request, pk):
    user = User.objects.get(id=pk)
    form = UserForm(instance=user)

    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            if request.POST.get('role') == 'student':
                return redirect('students')
            else:
                return redirect('teachers')  

    context = {'form':form}
    return render(request, 'form.html', context) 


def delete_user(request, pk):
    user = User.objects.get(id=pk)

    if request.method=='POST':
        user.delete()
        if user.role == 'student':
            return redirect('students')
        else:
            return redirect('teachers')  
    
    context = {'user':user}
    return render(request, 'delete.html', context)