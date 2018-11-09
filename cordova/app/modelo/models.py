from django.db import models

# Create your models here.
class Estudiante(models.Model):
	listaGenero = (
		('f', 'Femenino'),
		('m', 'Masculino')
		)
	nombres = models.CharField(max_length = 25)
	apellidos = models.CharField(max_length = 25)
	cedula = models.CharField(max_length = 10)
	genero = models.CharField(max_length = 15, choices = listaGenero, null=True)
	fechaNacimiento = models.DateField(unique_for_date= '', null = True, max_length = 50)
	correo = models.CharField(max_length = 30, null = True)
	estado = models.BooleanField(default = True)
