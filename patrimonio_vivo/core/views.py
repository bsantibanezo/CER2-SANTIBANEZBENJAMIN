from django.shortcuts import render

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