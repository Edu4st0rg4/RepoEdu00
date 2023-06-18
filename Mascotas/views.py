from django.shortcuts import render,redirect
from .models import Producto
from .forms import ProductoForm, RegistroUserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login

# Create your views here.
def inicio(request):
    return render(request, 'inicio.html')

def archivo_2(request):
    return render(request, 'archivo_2.html')

def archivo_3(request):
    return render(request, 'archivo_3.html')

def API(request):
    return render(request, 'API.html')

def formulario(request):
    return render(request, 'formulario.html')

def otra(request):
    productos= Producto.objects.raw('Select * from mascotas_producto')
    datos={
        'cositas':productos
    }
    return render(request, 'otra.html', datos)

def crear(request):
    if request.method=="POST":
        productoform = ProductoForm(request.POST,request.FILES)
        if productoform.is_valid():
            productoform.save()     #similar al insert
            return redirect('inicio')
    else:
        productoform=ProductoForm()
    return render(request, 'crear.html', {'productoform':productoform})

def eliminar(request, id):
    productoEliminado = Producto.objects.get(codigo=id) #obtenemos un objeto por su id
    productoEliminado.delete()
    return redirect ('otra')

def modificar(request, id):
    productoModificado = Producto.objects.get(codigo=id)
    datos = {
        'form': ProductoForm(instance=productoModificado) #devuelve el objeto instanciado de acuerdo al codigo
    }
    if request.method=='POST':
        formulario = ProductoForm(data=request.POST, instance=productoModificado)
        if formulario.is_valid:
            formulario.save()
            return redirect('otra')
    return render(request, 'modificar.html', datos)


def registrar(request):
    data={
        'form':RegistroUserForm()
    }
    if request.method=="POST":
        formulario = RegistroUserForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request,user)
            messages.success(request,"Te has registrado correctamente! uwu")
            return redirect('inicio')
        data["form"]=formulario #sobreescribimos el form
    return render(request, 'registration/registrar.html',data)

