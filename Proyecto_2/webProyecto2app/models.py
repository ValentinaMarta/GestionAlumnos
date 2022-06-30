from django.db import models

# Create your models here.
class Profesor(models.Model):
    name = models.CharField(max_length=255)
    tel = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    def __str__(self):
        return f'Profesor {self.id}: {self.name} {self.tel} {self.email}'



class Alumno(models.Model):
    name = models.CharField(max_length=255)
    tel = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    turno = models.CharField(max_length=255)
    def __str__(self):
        return f'Alumno {self.id}: {self.name} {self.tel} {self.email}{self.turno}'



class Calificaciones(models.Model):
    name = models.CharField(max_length=255)
    tel = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    nota1 = models.IntegerField()
    nota2 = models.IntegerField()
    media = models.IntegerField()
    Alumno = models.ForeignKey(Alumno, on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return f'Calificaciones {self.id}: {self.name} {self.tel} {self.email}{self.nota1}{self.nota2}'

class Grupo(models.Model):
    turno= models.CharField(max_length=255)
    Alumno = models.ManyToManyField(Alumno)
    def __str__(self):
        return f'Grupo {self.id}: {self.turno}'



