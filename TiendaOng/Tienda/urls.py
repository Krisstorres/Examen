from django.urls import path
from .views import Listar_prod, home,Contacto,QuienesSomos,Donaciones,Tiendas, Agregar_prod,Modificar_prod,Eliminar_prod

urlpatterns = [
    path('', home,name="home"),
    path('Contacto/', Contacto, name="contacto"),
    path('QuienesSomos/',QuienesSomos,name="Quienes somos"),
    path('Donaciones/',Donaciones,name="Donaciones"),
    path('Tiendas/',Tiendas,name="Tiendas"),
    #producto crud

    path('Agregar_prod/', Agregar_prod,name="Agregar"),

    path('Listar_prod/',Listar_prod,name="Listar"),

    path('Modificar_prod/<id>/',Modificar_prod,name="Modificar"),

    path('Eliminar_prod/<id>/',Eliminar_prod,name="Eliminar"),
]