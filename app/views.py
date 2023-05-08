from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

from .serializers import CoberturaSerializer, PlanSerializer, UsuarioSerializer
from .models import Cobertura, Plan

from django.contrib.gis.geos import Point
from django.contrib.auth.models import User as Usuario


class CoberturaList(generics.ListCreateAPIView):
    queryset = Cobertura.objects.all()
    serializer_class = CoberturaSerializer


class CoberturaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cobertura.objects.all()
    serializer_class = CoberturaSerializer


class PlanList(generics.ListCreateAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer


class PlanDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer


class UsuarioList(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class UsuarioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class LoginView(ObtainAuthToken):
    """
    Vista para el endpoint de inicio de sesión.

    Permite a los usuarios autenticarse y obtener un token de autenticación.

    Métodos:
    - post: Maneja las solicitudes POST para iniciar sesión.
    """

    def post(self, request, *args, **kwargs):
        """
        Maneja las solicitudes POST para iniciar sesión.

        Parámetros:
        - request: La solicitud HTTP recibida.
        - *args: Argumentos adicionales.
        - **kwargs: Argumentos de palabras clave adicionales.

        Retorna:
        - Una respuesta HTTP con el token de autenticación.
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key})


@api_view(["GET"])
def obtener_planes_disponibles(request):
    """
    Vista para el endpoint de obtener planes disponibles.

    Permite a los usuarios obtener una lista de planes disponibles basados en la ubicación.

    Parámetros:
    - request: La solicitud HTTP recibida.

    Retorna:
    - Una respuesta HTTP con la lista de planes disponibles.
    """
    latitud = request.query_params.get("latitud")
    longitud = request.query_params.get("longitud")
    punto = Point(float(longitud), float(latitud))
    planes_disponibles = Plan.objects.filter(coberturas__poligono__contains=punto)
    serializer = PlanSerializer(planes_disponibles, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def registrar_usuario(request):
    """
    Vista para el endpoint de registro de usuarios.

    Permite a los usuarios registrarse en la aplicación.

    Parámetros:
    - request: La solicitud HTTP recibida.

    Retorna:
    - Una respuesta HTTP con los datos del usuario registrado o los errores de validación.
    """
    serializer = UsuarioSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def crear_cobertura(request):
    """
    Vista para el endpoint de creación de cobertura.

    Permite a los usuarios crear una nueva cobertura.

    Parámetros:
    - request: La solicitud HTTP recibida.

    Retorna:
    - Una respuesta HTTP con los datos de la cobertura creada o los errores de validación.
    """
    data = request.data
    coordinates = data["location"]["coordinates"]
    longitud, latitud = map(float, coordinates)
    punto = Point(longitud, latitud)
    data["location"] = punto
    serializer = CoberturaSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def crear_plan(request):
    """
    Vista para el endpoint de creación de plan.

    Permite a los usuarios crear un nuevo plan.

    Parámetros:
    - request: La solicitud HTTP recibida.

    Retorna:
    - Una respuesta HTTP con los datos del plan creado o los errores de validación.
    """
    serializer = PlanSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
