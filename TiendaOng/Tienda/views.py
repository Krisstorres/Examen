from dataclasses import dataclass
import django
from django.forms import PasswordInput
from django.http import Http404
from django.shortcuts import get_object_or_404, render,redirect
from requests import Response
from .models import CATEGORIASS, Fundaciones, Productoww, Refugios1,Contacto, Refugios3
from .forms import ContactoForm, FundacionForm,ProductoForm,CustomUserCreationForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required,permission_required
from rest_framework import viewsets
from .serializers import ContactoSerializer, FundacionesSerializer, ProductosSerializer,CategoriaSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

class ProductoViewsets(viewsets.ModelViewSet):
    queryset=Productoww.objects.all()
    serializer_class=ProductosSerializer

class FundacionViewsets(viewsets.ModelViewSet):
    queryset=Refugios3.objects.all()
    serializer_class=FundacionesSerializer

class ContactoViewsets(viewsets.ModelViewSet):
    queryset=Contacto.objects.all()
    serializer_class=ContactoSerializer

class CategoriaViewsets(viewsets.ModelViewSet):
    queryset=CATEGORIASS.objects.all()
    serializer_class=CategoriaSerializer

       
        
# tEMPLATE TIENDA------------------------------------------------------------------------------------------
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
    fundaciones = Refugios3.objects.all()
    data ={'fundaciones':fundaciones}
    return render(request,'Tienda/Donaciones.html',data)

def QuienesSomos (request):
    return render(request,'Tienda/QuienesSomos.html')

def Tiendas (request):
    productos = Productoww.objects.all()
    data = {'productos':productos}

    return render(request,'Tienda/Tiendas.html',data)
# TEMPLATE TIENDA------------------------------------------------------------------------------------------
#--------------------------------------------------------------


# crud se crea primero el enñace template 
#luego se agrega el form     
# AGREGAR PRODUCTO------------------------------------------------------------------------------------------
@permission_required('Tienda.add_productoww')
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

# LISTAR PRODUCTO------------------------------------------------------------------------------------------
@permission_required('Tienda.view_productoww') 
def Listar_prod(request):
    productos = Productoww.objects.all()
    page=request.GET.get('page',1)
    try:
        paginator=Paginator(productos, 5)#se instancia el paginador y sel e da un maximo de 5 productos por pagina 
        productos=paginator.page(page)#paginador entregue la pagina que va por parametro 
    except:
        raise Http404 #si no encuentra la pagina se invoca la exception Http404. 

    data = {'entity':productos,
            'paginator':paginator
    
    }

    return render(request, 'Tienda/producto/Listar.html',data)

# Modificar------------------------------------------------------------------------------------------
@permission_required('Tienda.change_productoww')
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

# Eliminar producto------------------------------------------------------------------------------------------
@permission_required('Tienda.delete_productoww')
def Eliminar_prod(request,id):
    producto=get_object_or_404(Productoww,id=id)
    producto.delete()
    messages.success(request,"Producto Eliminado Correctamente")
    return redirect(to="Listar")


# FUndacion------------------------------------------------------------------------------------------
@permission_required('Tienda.add_fundaciones')
def Agregar_F(request):
    data={
        'forme':FundacionForm
    }
    if request.method == 'POST':
        formulario = FundacionForm(data=request.POST,files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"Fundacion Agragada Correctamente ")
        else:
            data['forme']=formulario
    return render(request, 'Tienda/producto/AgregarF.html',data)




def Registro(request):
    data={
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario=CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save() 
            user =authenticate(username=formulario.cleaned_data["username"],password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request,"Usuario registrado exitosamente")
            return redirect(to="home")

        data["form"] = formulario

    return render(request, 'registration/registrar.html',data)

@csrf_exempt
@api_view(['GET', 'POST'])
def lista_productos(request):
    if request.method=='GET':
        producto = Productoww.objects.all()
        serializer = ProductosSerializer(producto, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProductosSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


            
@api_view(['GET', 'PUT', 'DELETE']) 
def detalle_productos(request, id):
    try:
        producto= Productoww.objects.get(id=id)
    except Productoww.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ProductosSerializer(producto)
        return Response(serializer.data)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ProductosSerializer(producto, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        producto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)