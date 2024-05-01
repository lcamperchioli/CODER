from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Producto, Cliente
from .forms import ProductoForm, ClienteForm

def index(request):
    return render(request, 'index.html')

def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProductoForm()
    return render(request, 'agregar_producto.html', {'form': form})

def agregar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ClienteForm()
    return render(request, 'agregar_cliente.html', {'form': form})

def buscar(request):
    if request.method == 'POST':
        term = request.POST.get('termino_busqueda')
        resultados = Producto.objects.filter(nombre__icontains=term)
        return render(request, 'resultados_busqueda.html', {'resultados': resultados})
    else:
        return render(request, 'buscar.html')
