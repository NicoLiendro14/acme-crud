from rest_framework import serializers
from django.contrib.auth.models import User as Usuario
from .models import Cobertura, Plan

class CoberturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cobertura
        fields = '__all__'

class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
