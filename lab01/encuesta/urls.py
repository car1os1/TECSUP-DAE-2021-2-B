from django.urls import path
from django.urls.resolvers import URLPattern
from.import views
urlpatterns=[
    path('',views.index,name='index'),
    #localhots:8000/polls/6
    path('<int:pregunta_id>/',views.detalle,name='detail'),
    #localhots:8000/polls/6/results
    path('<int:pregunta_id>/results', views.resultados,name='results'),
    #localhots:8000/polls/6/vote
    path('<int:pregunta_id>/vote/', views.votar,name='vote'), 
]