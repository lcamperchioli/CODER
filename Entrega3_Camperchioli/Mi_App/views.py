from django.shortcuts import render

# Create your views here.
# En mi_app/views.py

from django.shortcuts import render
from .models import Clase1, Clase3
from .forms import Clase1Form, Clase3Form

def ingresar_datos(request):
    if request.method == 'POST':
        form1 = Clase1Form(request.POST)
        form3 = Clase3Form(request.POST)
        if form1.is_valid() and form3.is_valid():
            form1.save()
            form3.save()
    else:
        form1 = Clase1Form()
        form3 = Clase3Form()
    return render(request, 'ingresar_datos.html', {'form1': form1, 'form3': form3})

def buscar(request):
    if request.method == 'POST':
        query = request.POST.get('query')
        resultados = Clase1.objects.filter(campo1__icontains=query)
        # Puedes hacer lo mismo para las otras clases si quieres buscar en ellas también
        return render(request, 'resultados_busqueda.html', {'resultados': resultados})
    return render(request, 'buscar.html')
