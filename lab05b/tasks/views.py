from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import TaskForm
from .models import Tareas
# Create your views here.


def casa(request):
    return render(request, 'main.html')


def registro(request):

    if request.method == 'GET':
        print("enviando form")
        return render(request, 'registro.html', {
            'form': UserCreationForm
        })

    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('tareas')
            except IntegrityError:
                return render(request, 'registro.html', {
                    'form': UserCreationForm,
                    'error': 'el usuario ya existe elija otro nombre'
                })
        return render(request, 'registro.html', {
            'form': UserCreationForm,
            'error': 'las contraseñas no coiciden'
        })


def tareas(request):
    tareas = Tareas.objects.filter(user=request.user, completado__isnull=True)
    return render(request, 'tareas.html', {
        'tareas':tareas
    })


def salir(request):
    logout(request)
    return redirect('main')


def iniciaSesion(request):
    if request.method == 'GET':
        print("enviando form")
        return render(request, 'login.html', {
            'form': AuthenticationForm
        })

    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'login.html', {
                'form': AuthenticationForm,
                'error': "el usuario o la contraseña no existen"
            })
        else:
            login(request, user)
            return redirect('tareas')


def crearTarea(request):
    if request.method == 'GET':
        return render(request, 'crearTarea.html', {
            'form': TaskForm
        })
    else:
        form = TaskForm(request.POST)
        nueva_tarea = form.save(commit=False)
        nueva_tarea.user = request.user
        nueva_tarea.save()
        return redirect('tareas')
def tareaDetalle(request, id):
    tarea = get_object_or_404(Tareas, pk=id)
    return render(request, 'detalle.html', {
        'tarea': tarea
    })