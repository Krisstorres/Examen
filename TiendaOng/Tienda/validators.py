from inspect import classify_class_attrs
from sys import maxsize
from django.forms import ValidationError




class LargoMaximo:
    def __init__(self,max_file_size=5):
        self.max_file_size =max_file_size


    def __call__(self,value):
        size=value.size
        max_size=self.max_file_size*1048576

        if size > max_size:
            raise ValidationError(f"El archivo excede el tamaño maximo permitido:({self.max_file_size})MB")