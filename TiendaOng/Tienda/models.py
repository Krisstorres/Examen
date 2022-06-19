from distutils.command.upload import upload
from pickle import TRUE
from pyexpat import model
from tkinter import CASCADE
from django.db import models
from django.forms import IntegerField




class Marca(models.Model):
    id_marca=models.IntegerField(primary_key=True,verbose_name='ID Marca')
    nombre =models.CharField(max_length=50,blank=False,verbose_name='Nombre')
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