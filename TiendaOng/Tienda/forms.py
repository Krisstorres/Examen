from ast import Import, Pass
from dataclasses import field, fields
from email.mime import image
from genericpath import exists
from pyexpat import model
from tkinter import Widget
from django import forms
from .models import Contacto, Fundaciones, Productoww,Refugios2, Refugios3
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .validators import LargoMaximo


#se crea un nuevo archivo para guardar el formulario y encapsular las validaciones 
class ContactoForm(forms.ModelForm):
    class Meta:   
        model=Contacto
        #tiene que contener todo de lo contrario se caera el codigo por lo tanto conviene tener los campos siempre en modo 
        #not null 
        fields=["nombre","correo","tipo_consulta","mensaje"]
        # fields='__all__'
    
class ProductoForm(forms.ModelForm):    
    class Meta:
        model=Productoww
        fields='__all__'
        

    nombre=forms.CharField(max_length=50,min_length=7)
    precio=forms.IntegerField(min_value=15000 ,max_value=1500000)
    stock=forms.IntegerField(max_value=500)
    imagen=forms.ImageField(validators=[LargoMaximo(max_file_size=5)])




class FundacionForm(forms.ModelForm):
    class Meta: 
        model=Refugios3
        fields='__all__'





class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password1','password2']
        