from django.db import models


class CitaMedica(models.Model):
    dia = models.DateField()
    hora = models.DateTimeField()
    paciente = models.ForeignKey('Paciente', on_delete=models.CASCADE)
    medico = models.ForeignKey('Medico', on_delete=models.CASCADE)


class Paciente(models.Model):
    nombre = models.CharField(max_lenght=50)
    apellidoPaterno = models.CharField(max_lenght=50)
    apellidoMaterno = models.CharField(max_lenght=50)
    fechaNacimiento = models.DateField()
    talla = models.IntegerField(max_length=3)
    peso = models.IntegerField(max_length=2)


class Medico(models.Model):
    nombre = models.CharField(max_lenght=50)
    apellidoPaterno = models.CharField(max_lenght=50)
    apellidoMaterno = models.CharField(max_lenght=50)
    usuario = models.CharField(max_lenght=50)
    contraseña = models.CharField(max_lenght=50)
