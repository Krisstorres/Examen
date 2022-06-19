from dataclasses import dataclass
from django.shortcuts import get_object_or_404, render,redirect
from .models import Producto, Productoww
from .forms import ContactoForm,ProductoForm
from django.contrib import messages

# Create your views here.
def home (request):
    return render(request,'Tienda/home.html')

def Contacto (request):
    data ={
        'form' : ContactoForm()
        #se cre ainstancia del objeto (new)
    }
    if request.method == 'POST':
        formulario=ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"Contacto Realizado Correctamente")
        else:
            data['form']=formulario
    return render(request,'Tienda/Contacto.html',data)
    

def Donaciones (request):
    return render(request,'Tienda/Donaciones.html')

def QuienesSomos (request):
    return render(request,'Tienda/QuienesSomos.html')

def Tiendas (request):
    productos = Productoww.objects.all()
    data = {'productos':productos}

    return render(request,'Tienda/Tiendas.html',data)
#--------------------------------------------------------------

# crud se crea primero el enñace template 
#luego se agrega el form     
def Agregar_prod(request):
    data={
        'form': ProductoForm() 
        }

    if request.method =='POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"Producto Agregado Correctamente")
        else:
            data["form"]= formulario
    return render(request,'Tienda/producto/Agregar.html',data)


def Listar_prod(request):
    productos = Productoww.objects.all()
    data = {'productos':productos}
    return render(request, 'Tienda/producto/Listar.html',data)

def Modificar_prod(request,id):
    #instancia
    producto=get_object_or_404(Productoww, id = id)
    #producto=Productow.objects.get(id=id)
    data={
        'form':ProductoForm(instance=producto)
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"Producto Modificado Correctamente")
            return redirect(to="Listar")
        data['form']=formulario    
    return render(request, 'Tienda/producto/Modificar.html',data)


def Eliminar_prod(request,id):
    producto=get_object_or_404(Productoww,id=id)
    producto.delete()
    messages.success(request,"Producto Eliminado Correctamente")
    return redirect(to="Listar")