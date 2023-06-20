from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
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
                return redirect('tareas')
            except:
                return render(request, 'registro.html', {
                    'form': UserCreationForm,
                    'error': 'hubo un error inesperado'
                })
        return render(request, 'registro.html', {
            'form': UserCreationForm,
            'error': 'las contraseñas no coiciden'
        })


def tareas(request):
    return render(request, 'tareas.html')