from django.urls import path
from.import views
app_name='calculadora'

urlpatterns=[
    path('formulario',views.formulario,name='formulario'),
    path('respuesta',views.respuesta, name ='respuesta'),
    path('cilindro',views.cilindro,name='cilindro'),
    path('rpta',views.rpta,name='rpta'),
]