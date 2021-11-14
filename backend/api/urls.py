from django.urls import path

from . import views 

urlpatterns= [
    path('', views.index),
    path('prestamos', views.Prestamo),
    path('prestamos/<int:prestamo_id>',views.prestamodetalle)

]