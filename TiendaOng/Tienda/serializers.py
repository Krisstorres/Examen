#este archivo sera elque va a convertir los datos a json y va a permitir editar los datos en este formato         exclude=['nombre_campo']
from dataclasses import fields
from imp import source_from_cache
from pyexpat import model
from unittest.util import _MAX_LENGTH
from .models import  CATEGORIASS, Marca, Productoww, Refugios2,Contacto, Refugios3
from rest_framework import serializers



class MarcaSerializer(serializers.ModelSerializer):
    class Meta: 
        model=Marca
        fields='__all__'

class ProductosSerializer(serializers.ModelSerializer):
    marca=MarcaSerializer(read_only=True)
    marca_id=serializers.PrimaryKeyRelatedField(queryset=Marca.objects.all(),source="marca")
    categoria_nombre = serializers.CharField(source="categorias.nombre_categoriass")
    nombre=serializers.CharField(min_length=3)
    
 
    
    
    
    class Meta:
        model=Productoww
        fields='__all__'


class FundacionesSerializer(serializers.ModelSerializer):
    
    
    
    def Validate_name(self,value):
        nombre_refugio=serializers.CharField(required=True,min_lenght=7)
        
        
        existe=Refugios2.objects.filter(nombre_refugio__iexact=value).exists() #el __iexact =quita el case sensitive
        if existe:
            raise serializers.ValidationError("este producto ya se encuentra en la base de datos por favor ingresa uno con otro nombre")
        else:
            return value  
        
    class Meta:
        model=Refugios3
        fields='__all__'


class ContactoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Contacto
        fields='__all__'


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model=CATEGORIASS
        fields='__all__'


