from django.shortcuts import render

# Create your views here.
def formulario(request):
    return render(request,'calculadora/formulario.html')

def respuesta(request):
    a = request.POST['n1']
    b = request.Post['n2']
    suma = int(a)+ int(b)
    context ={
        'a' : a,
        'b' : b,
    'resultado' : suma        
    }
    return render(request,'calculadora/resultado.html',context)