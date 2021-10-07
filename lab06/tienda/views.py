from django.shortcuts import render,get_object_or_404
from .models import Producto,Categoria

# Create your views here.
def index(request):
    product_list = Producto.objects.order_by('nombre')[:6]
    categoria_list = Categoria.objects.order_by('nombre')[:7]
    context= {'product_list' : product_list}
    context={'categoria_list': categoria_list}
    return render(request,'index.html',context)

def producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    return render(request, 'producto.html', {'producto': producto})    
'''
def categoria(request):
    categoria_list = Categoria.objects.order_by('nombre')[:3]
    
    return render(request,'index.html',context)
'''