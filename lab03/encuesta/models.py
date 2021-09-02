from django.db import models

class Pregunta(models.Model):
    pregunta_texto = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Option(models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    opcion_texto = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)