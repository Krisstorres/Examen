from dataclasses import field, fields
from tkinter import Widget
from django import forms
from .models import Contacto, Productoww
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
        Widgets={"fecha_fabricacion":forms.SelectDateWidget()}


