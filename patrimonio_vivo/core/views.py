from django.shortcuts import render

# Create your views here.

def inicio(request):
    contexto = {'nombre': 'Benjamín'}
    return render(request, 'core/inicio.html', contexto)
