from django.contrib.auth.decorators import login_required
from django.forms import modelform_factory
from django.shortcuts import render, redirect

from webProyecto2app.models import *
from webProyecto2app.forms import AlumnForm


def login(request):
    return render(request, 'index.html', {})

def extraeralumno(request):
    nro_alumnos = Alumno.objects.count()
    #notas = Calificaciones.objects.all()
    alumno = Alumno.objects.all()
    return render(request, 'Grupo1.html', {'nro_alumnos': nro_alumnos, 'alumno': alumno})
    #'par_notas': notas


def notasalumno(request, id):
    notas = Calificaciones.objects.objects.all()
    calif = Calificaciones.objects.get(pk=id)
    return render(request, 'notas.html', {'notas': notas, 'calif': calif})



@login_required
def nuevoalumno(request):
    if request.method == 'POST':
        formaAlumno = AlumnForm(request.POST)
        if formaAlumno.is_valid():
            formaAlumno.save()
            return redirect('Grupo1')
    else:
        formaAlumno = AlumnForm

    return render(request, 'nuevoalumno.html', {'formaAlumno': formaAlumno})


# Create your views here.

