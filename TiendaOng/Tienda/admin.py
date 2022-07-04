from django.contrib import admin

from Tienda.models import Marca, Productoww
from .models import Contacto, Fundaciones, Marca,Productoww,CATEGORIASS
class ProductoAdmin(admin.ModelAdmin):
    list_display=["nombre","precio","marca","nuevo","imagen"]
    list_editable=["precio"]
    search_fields=["nombre"]
    list_filter=["marca","nuevo","nombre"]
    list_per_page=5
# Register your models here.
admin.site.register(Marca)
admin.site.register(Productoww,ProductoAdmin)
admin.site.register(Contacto)
admin.site.register(CATEGORIASS)
admin.site.register(Fundaciones)
