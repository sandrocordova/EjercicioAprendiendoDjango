from django.shortcuts import render, redirect
from django.http import HttpResponse
#from django.contrib.auth.decorators import login_required
from .forms import FormularioEstudiante
from app.modelo.models import Estudiante

def  principal(request):
	lista2=""
	listaClientes = Estudiante.objects.all().filter(estado=True).order_by("apellidos")

	context={
		'lista':listaClientes
	}
	return render(request, 'estudiante/principal_estudiante.html', context)

def  lista(request):
	#httpresponse envía un mensaje
	return HttpResponse("Primer Mensaje")


def  crear(request):
	formulario = FormularioEstudiante(request.POST)

	if request.method == "POST":
		if formulario.is_valid():
			datos = formulario.cleaned_data
			cliente = Cliente()
			cliente.nombres = datos.get("nombres")
			cliente.apellidos = datos.get("apellidos")
			cliente.cedula = datos.get('cedula')
			cliente.genero = datos.get("genero")
			cliente.fechaNacimiento = datos.get("fechaNacimiento")
			cliente.correo = datos.get("correo")
			cliente.save()
			print("guardooooooooooooooooooooooooooooooo")
			return redirect(lista)
	context = {
	'f':formulario,
	'mensaje':'Bienvenidos',
	}
#utilizamos render porque ya no quiero mostrar un mensaje
	return render(request, "estudiante/crear_estudiante.html", context)
