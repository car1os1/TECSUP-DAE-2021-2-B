from datetime import date
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import prestamo
from .serializers import PrestamoSerializer
# Create your views here.


@api_view(['GET'])
def index(request):
    return Response({'mensaje':'api rest de prestamo de libros '})

@api_view(['GET','POST'])
def Prestamo(request):
    if request.method == 'GET':
        lstPrestamo = prestamo.objects.all()
        serPrestamo = PrestamoSerializer(lstPrestamo,many=True)
        return Response (serPrestamo.data)
    elif request.method =='POST':
        serPrestamo = PrestamoSerializer(data=request.data)
        if serPrestamo.is_valid():
            serPrestamo.save()
            return Response(serPrestamo.data)
        else:
            return Response(serPrestamo.erros)

@api_view(['GET','PUT','DELETE'])
def prestamodetalle(request,prestamo_id):
    objPrestamo = prestamo.objects.get(id=prestamo_id)

    if request.method == 'GET':
        serPrestamo = PrestamoSerializer(objPrestamo)
        return Response(serPrestamo.data)  
    elif request.method == 'PUT':
        serPrestamo = PrestamoSerializer(objPrestamo,date=request.data)
        if serPrestamo.is_valid():
            serPrestamo.save()
            return Response(serPrestamo.data)
        else:
            return Response(serPrestamo.errors)
        
    if request.method =='DELETE':
        objPrestamo.delete()
        return Response(status=204)