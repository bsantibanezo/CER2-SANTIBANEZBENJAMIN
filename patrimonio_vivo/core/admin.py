from django.contrib import admin
from .models import Categoria, LugarPatrimonial

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion']

@admin.register(LugarPatrimonial)
class LugarPatrimonialAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'ubicacion', 'anio_construccion', 'categoria']
    list_filter = ['categoria']
    search_fields = ['nombre', 'descripcion']