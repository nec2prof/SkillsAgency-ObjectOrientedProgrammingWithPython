from django.shortcuts import render
from django.http import HttpResponse
import os

url_base = os.path.abspath(os.path.dirname)

# Create your views here.
def inicio(request):
    # return HttpResponse('Home')
    return render(request, 'app_cfp016/templates/home.html')

def cursos(request):
    # return HttpResponse('Cursos')
    return render(request, 'app_cfp016/templates/cursos.html')

def profesores(request):
    # return HttpResponse('Profesores')
    return render(request, 'app_cfp016/templates/profesores.html')

def estudiantes(request):
    # return HttpResponse('Estudiantes')
    return render(request, 'app_cfp016/templates/estudiantes.html')

def entregables(request):
    # return HttpResponse('Entregables')
    return render(request, 'app_cfp016/templates/entregables.html')
