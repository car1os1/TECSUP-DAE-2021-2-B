from django.urls import path
from django.urls.resolvers import URLPattern
from.import views
urlpatterns=[
    path('',views.suma,name='suma'),

    path('<int:valor_id>/<int:valor2>',views.valor1,name='valor1'),

    path('<int:valor_id>/<int:valor2>/resta/',views.valor2,name='valor2'),

    path('<int:valor_id>/<int:valor2>/multi/',views.valor3,name="valor3")
]