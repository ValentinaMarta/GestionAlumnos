from django.shortcuts import render

from webProyecto2app.models import *

def login(request):
    return render(request, 'index.html', {})

def extraeralumno(request):
    nro_alumnos = Alumno.objects.count()
    notas = Calificaciones.objects.all()
    alumno = Alumno.objects.all()
    return render(request, 'calificaciones.html', {'nro_alumnos': nro_alumnos, 'alumno': alumno, 'par_notas': notas})

# Create your views here.

