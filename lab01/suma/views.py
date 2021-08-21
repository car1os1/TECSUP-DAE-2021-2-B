from django import http
from django.shortcuts import render
from django.http import HttpResponse, response
# Create your views here.


def suma(request):
    return HttpResponse("bienvenido a sumeitor" )

def valor1(request,valor_id,valor2):
    suma=valor_id+valor2
    respuesta= "la suma es " +str(suma)
    return HttpResponse(respuesta)

def valor2(request,valor_id,valor2):
    resta=valor_id-valor2
    respuesta= "la resta es " +str(resta)
    return HttpResponse(respuesta)

def valor3(request,valor_id,valor2):
    multi=valor_id*valor2
    respuesta= "la multiplicacion es " +str(multi)
    return HttpResponse(respuesta)