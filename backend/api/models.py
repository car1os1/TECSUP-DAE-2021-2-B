from django.db import models

# Create your models here.
class prestamo(models.Model):
    FICCION = 'ficcion'
    JUVENILES = 'juveniles'
    CIENTIFICOS  ='cientificos'

    CATEGORIA_CHOICES =(
        (FICCION, 'ficcion'),
        (JUVENILES, 'juveniles'),
        (CIENTIFICOS,'cientificos'),
    )

    libro  = models.CharField(max_length=200)
    category = models.CharField(max_length=20,choices=CATEGORIA_CHOICES)
    fechapre = models.DateTimeField(auto_now=False)
    fechadev = models.DateTimeField(auto_now=False)

    def __str__(self):
        return libro