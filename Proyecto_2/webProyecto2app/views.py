from django.shortcuts import render

from webProyecto2app.models import *

def login(request):
    return render(request, 'index.html', {})

def extraeralumno(request):
    nro_alumnos = Alumno.objects.count()
    #notas = Calificaciones.objects.all()
    alumno = Alumno.objects.all()
    return render(request, 'Grupo1.html', {'nro_alumnos': nro_alumnos, 'alumno': alumno})
    #'par_notas': notas

"""def notasalumno(request, id):
    nro_alumnos = Alumno.objects.count()
    alumno = Alumno.objects.get(pk=id)
    notas = Calificaciones.objects.all()
    return render(request, 'notas.html', {'nro_alumnos': nro_alumnos, 'alumno': alumno, 'notas': notas})"""

def notasalumno(request):

    notas = Calificaciones.objects.all()
    return render(request, 'notas.html', {'notas': notas})

# Create your views here.

