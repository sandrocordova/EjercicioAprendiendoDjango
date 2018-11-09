from django import forms
from app.modelo.models import Estudiante

class FormularioEstudiante(forms.ModelForm):
	""""
	PAra hacer el mapeo se utiliza meta"""
	class Meta: 
		model = Estudiante
		fields = ["nombres","apellidos","cedula","genero","fechaNacimiento","correo"]