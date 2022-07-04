from django.urls import path,include
from .views import Agregar_F, Listar_prod, detalle_productos, home,Contacto,QuienesSomos,Donaciones,Tiendas,\
Agregar_prod,Modificar_prod,Eliminar_prod,Registro,ProductoViewsets,FundacionViewsets,ContactoViewsets,CategoriaViewsets, lista_productos
from rest_framework import routers
#generacion de urls de listar elimnar y modificar para que las registrar en el path 
router= routers.DefaultRouter()
router.register('producto',ProductoViewsets)
router.register('fundaciones',FundacionViewsets)
router.register('Contactos',ContactoViewsets)
router.register('Categorias',CategoriaViewsets)







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
    path('Agregar_F/',Agregar_F,name="Agregar_F"),
    #user
    path('Registrar/',Registro,name="Registro"),
    #api rest 
    path('api/',include(router.urls)),
    path('lista_productos', lista_productos, name= "lista_productos"),
    path('detalle_productos/<id>', detalle_productos, name="detalle_productos"),
 



]