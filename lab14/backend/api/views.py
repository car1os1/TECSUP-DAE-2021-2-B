from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# Create your views here.
@api_view(['GET'])
def publico(request):
    data = {
        'mensaje' : 'acceso publico'
    }
    return Response(data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def privado(request):
    data = {
        'mensaje' : 'acceso con autenticacion de usuario '
    }
    return Response(data)
