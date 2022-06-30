from django.shortcuts import render
from webProyecto2app.models import *


def extraeralumno(request):
    nro_alumnos = Alumno.objects.count()
    alumno = Alumno.objects.all()
    return render(request, 'index.html',{'nro_alumnos': nro_alumnos, 'alumno': alumno})

# Create your views here.

