from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import campanaForm,CustomUserCreationForm
from .models import Campana
from django.contrib import messages
from django.utils import timezone


def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': CustomUserCreationForm()
        })
    else:
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            try:
                user = form.save()
                login(request, user)
                return redirect('campana')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': form,
                    'error': 'El usuario ya existe'
                })
        else:
            # Muestra todos los errores que tiene el formulario
            return render(request, 'signup.html', {
                'form': form,
                'error': form.errors  # Muestra los errores del formulario directamente
            })

def campana(request):
    campana = Campana.objects.filter(
        user=request.user, fechaTermino__isnull=True)
    return render(request, 'campana.html',
                  {'campana': campana})
    
def campana_finalizada(request):
    campana = Campana.objects.filter(user=request.user, fechaTermino__isnull=False).order_by('-fechaTermino')
    return render(request, 'campana.html', {'campana': campana})

def crear_campana(request):
    if request.method == 'GET':
        return render(request, 'crear_campana.html', {'form': campanaForm()})
    else:
        try:
            form = campanaForm(request.POST)
            nueva_campana = form.save(commit=False)
            nueva_campana.user = request.user
            nueva_campana.save()
            return redirect('campana')
        except ValueError:
            return render(request, 'crear_campana.html', {
                'form': campanaForm(),
                'error': 'Por favor ingresa datos válidos'
            })


def detalle_campana(request, id_campana):
    if request.method == 'GET':
        campana = get_object_or_404(Campana, pk=id_campana, user=request.user)
        form = campanaForm(instance=campana)
        return render(request, 'detalle_campana.html', {
            'campana': campana,
            'form': form
        })
    else:
        try:
            campana = get_object_or_404(Campana, pk=id_campana, user=request.user)
            form = campanaForm(request.POST, instance=campana)
            form.save()
            messages.success(request, "La campaña se actualizó con éxito.")  # Agregar mensaje de éxito
            return redirect('campana')
        except ValueError:
            form = campanaForm(instance=campana)
            messages.error(request, "Error al actualizar la campaña.")  # Agregar mensaje de error
            return render(request, 'detalle_campana.html', {
                'campana': campana,
                'form': form,
                'error': "Error actualizando la campaña"
            })


def campana_completada(request, id_campana):
    campana = get_object_or_404 (Campana, pk=id_campana)
    if request.method == 'POST':
        campana.fechaTermino = timezone.now()
        campana.save()
        return redirect('campana')
    
def campana_eliminada(request, id_campana):
    campana = get_object_or_404 (Campana, pk=id_campana)
    if request.method == 'POST':
        campana.delete()
        return redirect('campana')

def signout(request):
    logout(request)
    return redirect('home')

def inicio(request):
    if request.method == 'GET':
        return render(request, 'inicio.html', {
            'form': AuthenticationForm()  
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'inicio.html', {
                'form': AuthenticationForm(),
                'error': 'Usuario o contraseña incorrectos'
            })
        else:
            login(request, user)
            return redirect('home')

