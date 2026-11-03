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