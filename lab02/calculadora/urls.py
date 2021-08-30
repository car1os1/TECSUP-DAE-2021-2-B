from django.urls import path
from.import views
app_name='calculadora'

urlpatterns=[
    path('formulario',views.formulario,name='formulario'),
    path('respuesta',views.respuesta, name ='respuesta'),
]