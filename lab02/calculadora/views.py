from django.shortcuts import render
import math
# Create your views here.
def formulario(request):
    return render(request,'calculadora/formulario.html')

def cilindro(request):
    return render(request,'calculadora/cilindro.html')

def respuesta(request):
    a = request.POST['n1']
    b = request.POST['n2']
    suma = int(a)+ int(b)
    resta = int(a)- int(b)
    multi = int(a)* int(b)
    divi = int(a)/int(b)
    context ={
        'a' : a,
        'b' : b,
    'resultado' : suma ,
    'rresultado' : resta,    
    'xresultado' : multi,
    'diviresultado' : divi
    }
    return render(request,'calculadora/respuesta.html',context)
def rpta(request):
    radio = request.POST['radio']
    altura= request.POST['altura']
    volumen=(math.pi)*(pow(float(radio),2)*float(altura))
    context ={
        'altura' : altura,
        'diametro': radio,
        'volumen' : volumen
    }
    return render(request,'calculadora/rpta.html',context)