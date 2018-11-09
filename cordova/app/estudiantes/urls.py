#el controlador es el view
from django.urls import path

from . import views

urlpatterns = [
	path("", views.principal, name = "clientes"),
	path("lista", views.principal, name = "clientes"),
	path("nuevo", views.crear, name = "clientes"),
]