from django.db import models

# Create your models here.
class Profesor(models.Model):
    name = models.CharField(max_length=255)
    tel = models.CharField(max_length=255)
    email = models.CharField(max_length=255)


class Alumno(models.Model):
    name = models.CharField(max_length=255)
    tel = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    turno = models.CharField(max_length=255)



class Calificaciones(models.Model):
    name = models.CharField(max_length=255)
    tel = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    nota1 = models.IntegerField()
    nota2 = models.IntegerField()
    media = models.IntegerField()

class Grupo(models.Model):
    turno= models.CharField(max_length=255)