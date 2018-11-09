from django.contrib import admin

from .models import Estudiante

class AdminEstudiante(admin.ModelAdmin):
	list_display= ["cedula","apellidos","nombres","genero", "fechaNacimiento"]
	#list_editable = ["apellidos","nombres"]
	#list_filter = ["genero"]
	#search_fields = ["cedula"]

	class Meta: 
		model = Estudiante

admin.site.register(Estudiante, AdminEstudiante)
	