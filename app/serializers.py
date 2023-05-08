from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Cobertura, Plan


class CoberturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cobertura
        fields = "__all__"


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo User.
    """

    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["username", "password"]

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class UserRegistrationSerializer(serializers.ModelSerializer):
    """
    Serializador para el registro de usuarios.
    """

    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["username", "password"]

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
