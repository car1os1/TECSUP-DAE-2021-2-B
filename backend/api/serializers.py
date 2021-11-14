from django.db import models
from rest_framework import serializers
from .models import prestamo


class PrestamoSerializer(serializers.ModelSerializer):
    class Meta:
        model = prestamo
        fields = '__all__'
