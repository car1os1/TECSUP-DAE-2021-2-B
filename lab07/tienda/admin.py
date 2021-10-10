from django.contrib import admin

# Register your models here.
from .models import Categoria,Producto

admin.site.register(Categoria)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('categoria','nombre','precio','stock')
admin.site.register(Producto,ProductoAdmin)