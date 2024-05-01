# En mi_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('ingresar-datos/', views.ingresar_datos, name='ingresar_datos'),
    path('buscar/', views.buscar, name='buscar'),
]
