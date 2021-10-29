from django.db import models
from rest_framework import fields, serializers
from .models import Producto

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto   
        fields = "__all__"