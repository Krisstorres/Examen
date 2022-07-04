from codecs import backslashreplace_errors
from distutils.command.upload import upload
from pickle import TRUE
from pyexpat import model
from tkinter import CASCADE
from django.db import models
from django.forms import IntegerField
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser




class Marca(models.Model):
    id_marca=models.IntegerField(primary_key=True,verbose_name='ID Marca')
    nombre=models.CharField(max_length=50,blank=False,verbose_name='Nombre')
    def __str__(self):
        return(self.nombre)

class Producto(models.Model):
    id_producto=models.CharField(max_length=50,primary_key=True,verbose_name='ID Producto')
    nombre=models.CharField(max_length=50,blank=False,verbose_name='Nombre producto')
    descripcion=models.TextField(max_length=50,blank=False,verbose_name='Descripcion producto')
    precio=models.IntegerField(blank=False,verbose_name='Precio producto')
    nuevo=models.BooleanField(blank=False,verbose_name='Nuevo')
    marca=models.ForeignKey(Marca,on_delete=models.PROTECT)
    fecha_fabricacion=models.DateField(blank=False,verbose_name='Fecha fabricacion')
    imagen=models.ImageField(upload_to="productos",null=True)
    def __str__(self):
        return(self.id_producto)

opciones_consultas=[
    [0,"consulta"],
    [1,"reclamo"],
    [2,"sugerencia"],
    [3,"felicitaciones"]
]


class Contacto(models.Model):
    nombre=models.CharField(max_length=50,blank=False,verbose_name='Nombre contactante')
    correo=models.EmailField(verbose_name='Correo contactante',blank=False)
    tipo_consulta=models.IntegerField(verbose_name='Motivo de contacto',blank=False,choices=opciones_consultas)
    mensaje=models.TextField(max_length=100,blank=True,verbose_name='Mensaje')
   

    def __str__(self):
        return self.nombre    

class Productow(models.Model):
    nombre=models.CharField(max_length=50,blank=False,verbose_name='Nombre producto')
    descripcion=models.TextField(max_length=50,blank=False,verbose_name='Descripcion producto')
    precio=models.IntegerField(blank=False,verbose_name='Precio producto')
    nuevo=models.BooleanField(blank=False,verbose_name='Nuevo')
    marca=models.ForeignKey(Marca,on_delete=models.PROTECT)
    fecha_fabricacion=models.DateField(blank=False,verbose_name='Fecha fabricacion')
    imagen=models.ImageField(upload_to="productos",null=True)
    def __str__(self):
        return(self.id_producto)

class CATEGORIASS(models.Model):
    nombre_categoriass=models.CharField(max_length=25,blank=False,verbose_name='Nombre Categoria')
    def __str__(self):
           return(self.nombre_categoriass)
class Productoww(models.Model):
    nombre=models.CharField(max_length=50,blank=False,verbose_name='Nombre producto')
    descripcion=models.TextField(max_length=50,blank=False,verbose_name='Descripcion producto')
    precio=models.IntegerField(blank=False,verbose_name='Precio producto')
    nuevo=models.BooleanField(blank=False,verbose_name='Nuevo')
    marca=models.ForeignKey(Marca,on_delete=models.PROTECT)
    fecha_fabricacion=models.DateField(blank=False,verbose_name='Fecha fabricacion')
    imagen=models.ImageField(upload_to="productos",null=True)
    stock=models.IntegerField(blank=False,verbose_name='Stock producto')
    categorias=models.ForeignKey(CATEGORIASS,on_delete=models.PROTECT)
    def __str__(self):
        return(self.nombre)



class Fundaciones(models.Model):
    nombre_fundacion=models.CharField(max_length=50,blank=False,verbose_name='Nombre Fundacion')
    rut_fundacion=models.CharField(max_length=50,blank=False,verbose_name='Rut Fundacion')
    foto_imagen=models.ImageField(upload_to="productos",null=True)
    cuenta_fundacion=models.IntegerField(blank=False,verbose_name='Numero de cuenta')
    def __str__(self):
        return(self.nombre_fundacion)
#--------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------







class Refugios1(models.Model):
    id_refugio=models.IntegerField(primary_key=True,verbose_name='ID_Fundacion')
    nombre_refugio=models.CharField(max_length=50,blank=False,verbose_name='Nombre de Refugio')
    descripcion_refugio=models.CharField(max_length=60,blank=False,verbose_name='Descripcion de refugio')
    subscrito=models.BooleanField(blank=False,verbose_name='Nuevo')
    imagen_refugio=models.ImageField(upload_to="productos",null=True)
    cuenta_refugio=models.IntegerField(verbose_name='Cuenta de fundacion',blank=False)
    rut_refugio=models.IntegerField(verbose_name='Rut de fundacion',blank=False)

    def __str__(self):
        return(self.nombre_refugio)
class Users(models.Model):
    usuario = models.ForeignKey(User,on_delete=models.PROTECT)
    donó=models.ForeignKey(Refugios1,on_delete=models.PROTECT)


class Refugios2(models.Model):
    id_refugio=models.IntegerField(primary_key=True,verbose_name='ID_Fundacion')
    nombre_refugio=models.CharField(max_length=50,blank=False,verbose_name='Nombre de Refugio')
    descripcion_refugio=models.CharField(max_length=60,blank=False,verbose_name='Descripcion de refugio')
    imagen_refugio=models.ImageField(upload_to="productos",null=True)
    cuenta_refugio=models.IntegerField(verbose_name='Cuenta de fundacion',blank=False)
    rut_refugio=models.IntegerField(verbose_name='Rut de fundacion',blank=False)

    def __str__(self):
        return(self.nombre_refugio)
class Users1(models.Model):
    usuario = models.ForeignKey(User,on_delete=models.PROTECT)
    donó=models.BooleanField(verbose_name='Donador?',blank=False)



class Refugios3(models.Model):
    id_refugio=models.IntegerField(primary_key=True,verbose_name='ID_Fundacion')
    nombre_refugio=models.CharField(max_length=50,blank=False,verbose_name='Nombre de Refugio')
    descripcion_refugio=models.CharField(max_length=60,blank=False,verbose_name='Descripcion de refugio')
    imagen_refugio=models.ImageField(upload_to="productos",null=True)
    cuenta_refugio=models.IntegerField(verbose_name='Cuenta de fundacion',blank=False)
    rut_refugio=models.CharField(verbose_name='Rut de fundacion',blank=False,max_length=70)

    def __str__(self):
        return(self.nombre_refugio)



class Usuario_s(AbstractBaseUser):
    username=models.CharField(verbose_name='Nombre de usuario',unique=True,max_length=100)
    email=models.EmailField(verbose_name='Correo electronico',max_length=154,unique=True)
    nombres=models.CharField(verbose_name='Nombres',max_length=200,blank=True,null=False)
    apellidos=models.CharField(verbose_name='Apellidos',max_length=200,blank=False,null=False)
 
    def __str__(self):
        return (self.nombres)
# class Categorias1:
#     id_categoria=models.Integerfield(max_value=20,primary_key=True,verbose_name='ID_producto')
#     nombre_categoria=models.Charfield(max_length=50,blank=False,verbose_name='Nombre de categoria')


#     def __str__(self):
#         return(self.nombre_categoria)

# class Marca1:
#     id_marca=models.Integerfield(max_value=20,primary_key=True,verbose_name='ID_producto')
#     nombre_marca=models.Charfield(max_length=60,blank=False,verbose_name='Nombre de marca')

#     def __str__(self):
#         return(self.nombre_producto)

# class Producto1:
#     id_producto=models.Integerfield(max_value=20,primary_key=True,verbose_name='ID_producto')
#     nombre_producto=models.Charfield(max_length=50,min_length=7,verbose_name='Nombre de producto',blank=False)
#     descripcion_producto=models.Charfield(max_lenght=60,verbose_name='Descripcion de producto',blank=False)
#     marca=models.ForeingKey(Marca,on_delete=models.PROTECT)
#     categoria=models.ForeingKey(Categorias1,on_delete=models.PROTECT)
#     imagen_producto=models.ImageField(upload_to="productos",null=True)

#     def __str__(self):
#         return(self.nombre_producto)


