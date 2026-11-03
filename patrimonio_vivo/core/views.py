from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, get_object_or_404, redirect
from .forms import LugarForm

from django.shortcuts import get_object_or_404, render

from .models import LugarPatrimonial

# Create your views here.

def inicio(request):
    contexto = {'nombre': 'Benjamín'}
    return render(request, 'core/inicio.html', contexto)

def inicio(request):
    contexto = {'nombre': 'Benjamín'}
    return render(request, 'core/inicio.html', contexto)


def catalogo(request):
    lugares = LugarPatrimonial.objects.select_related('categoria')
    return render(request, 'core/catalogo.html', {'lugares': lugares})

def detalle(request, pk):
    lugar = get_object_or_404(LugarPatrimonial.objects.select_related('categoria'), pk=pk)
    return render(request, 'core/detalle.html', {'lugar': lugar})

@login_required
def gestion(request):
    lugares = LugarPatrimonial.objects.select_related('categoria').order_by('nombre')
    return render(request, 'core/gestion.html', {'lugares': lugares})


@login_required
@permission_required('core.add_lugarpatrimonial', raise_exception=True)
def lugar_crear(request):
    if request.method == 'POST':
        form = LugarForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Lugar agregado correctamente.')
            return redirect('gestion')
    else:
        form = LugarForm()
    return render(request, 'core/lugar_form.html', {'form': form, 'titulo': 'Agregar lugar'})


@login_required
@permission_required('core.change_lugarpatrimonial', raise_exception=True)
def lugar_editar(request, pk):
    lugar = get_object_or_404(LugarPatrimonial, pk=pk)
    if request.method == 'POST':
        form = LugarForm(request.POST, instance=lugar)
        if form.is_valid():
            form.save()
            messages.success(request, 'Lugar actualizado correctamente.')
            return redirect('gestion')
    else:
        form = LugarForm(instance=lugar)
    return render(request, 'core/lugar_form.html', {'form': form, 'titulo': 'Editar lugar'})