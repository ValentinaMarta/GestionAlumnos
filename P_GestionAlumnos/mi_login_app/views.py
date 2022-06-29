from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def bienvenido(request):
    return HttpResponse('Hola')
def despedida(request):
    return HttpResponse('Adios')