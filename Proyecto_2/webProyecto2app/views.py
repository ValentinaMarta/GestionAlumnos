
from django.shortcuts import render, redirect, get_object_or_404

from webProyecto2app.forms import AlumnoForm, CalificacionesForm
from webProyecto2app.models import *



def login(request):
    return render(request, 'index.html')


def datosAlumnos(request):
    nro_alumnos = Alumno.objects.count()
    alumno = Alumno.objects.all()
    return render(request, 'datosAlumnos.html', {'nro_alumnos': nro_alumnos, 'alumno': alumno})

def datosCalificaciones(request):
    notas = Calificaciones.objects.all()
    return render(request, 'datosCalificaciones.html', { 'notas': notas})


def agregarAlumno(request):
    if request.method == 'POST':
        formaAlumno = AlumnoForm(request.POST)
        if formaAlumno.is_valid():
            formaAlumno.save()
            return redirect('listaDatosAlumnos')
    else:
        formaAlumno = AlumnoForm

    return render(request, 'nuevoalumno.html', {'formaAlumno': formaAlumno})



def editarAlumno(request, id):
    alumno = get_object_or_404(Alumno, pk=id)
    if request.method == 'POST':
        formaAlumno = AlumnoForm(request.POST, instance=alumno)
        if formaAlumno.is_valid():
            formaAlumno.save()
            return redirect('listaDatosAlumnos')
    else:
        formaAlumno = AlumnoForm(instance=alumno)
    return render(request, 'editar.html', {'formaAlumno': formaAlumno})


def editarCalificaciones(request, id):
    notas = get_object_or_404(Calificaciones, pk=id)
    if request.method == 'POST':
        formaCalifica = CalificacionesForm(request.POST, instance=notas)
        if formaCalifica.is_valid():
            formaCalifica.save()
            return redirect('enlaceDatosCalificaciones')
    else:
        formaCalifica = CalificacionesForm(instance=notas)
    return render(request, 'editarCalificaciones.html', {'formaCalifica': formaCalifica})


def eliminarAlumno(request, id):
    alumno = get_object_or_404(Alumno, pk=id)
    if alumno:
        alumno.delete()
    return redirect('listaDatosAlumnos')


def eliminarCalificaciones(request, id):
    notas = get_object_or_404(Calificaciones, pk=id)
    if notas:
        notas.delete()
    return redirect('enlaceDatosCalificaciones')


def agregarCalificaciones(request):
    if request.method == 'POST':
        formaCalificaciones = CalificacionesForm(request.POST)
        if formaCalificaciones.is_valid():
            formaCalificaciones.save()
            return redirect('enlaceDatosCalificaciones')
    else:
        formaCalificaciones = CalificacionesForm

    return render(request, 'nuevaCalificacion.html', {'formaCalificaciones': formaCalificaciones})



# Create your views here.

