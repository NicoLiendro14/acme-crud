import json

from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.serializers import AuthTokenSerializer


from .serializers import (
    CoberturaSerializer,
    PlanSerializer,
    UserSerializer,
)
from .models import Cobertura, Plan

from django.contrib.auth.models import User as Usuario
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import D
from django.contrib.gis.geos import GEOSGeometry
from django.contrib.auth.models import User


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
    serializer_class = UserSerializer


class UsuarioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UserSerializer


class RegisterView(APIView):
    """
    Vista para el registro de usuarios.

    Permite a los usuarios registrarse y obtener un token de autenticación.

    Métodos:
    - post: Maneja las solicitudes POST para el registro de usuarios.
    """

    @permission_classes([])
    def post(self, request, format=None):
        """
        Maneja las solicitudes POST para el registro de usuarios.

        Parámetros:
        - request: La solicitud HTTP recibida.
        - format: El formato de la respuesta HTTP.

        Retorna:
        - Una respuesta HTTP con el token de autenticación.
        """
        username = request.data.get("username")
        password = request.data.get("password")

        if username and password:
            # Verificar si el usuario ya existe
            try:
                user = User.objects.get(username=username)
                return Response({"error": "El usuario ya existe."})
            except User.DoesNotExist:
                # Crear el usuario si no existe
                user = User.objects.create_user(username=username, password=password)

                token, _ = Token.objects.get_or_create(user=user)

                return Response({"token": token.key})
        else:
            return Response(
                {"error": "No se proporcionaron nombre de usuario y contraseña."}
            )


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
@permission_classes([IsAuthenticated])
def obtener_planes_disponibles(request):
    """
    Vista para el endpoint de obtener planes disponibles.

    Permite a los usuarios obtener una lista de planes disponibles basados en la ubicación.

    Parámetros:
    - request: La solicitud HTTP recibida.

    Retorna:
    - Una respuesta HTTP con la lista de planes disponibles.

    Descripción:
    - Esta vista recibe la latitud y longitud de la ubicación del usuario en los parámetros de la solicitud GET.
    - Luego, se crea un punto geográfico a partir de las coordenadas proporcionadas.
    - A continuación, se filtran las coberturas que contienen el punto geográfico dentro de su polígono utilizando la función `distance_lte` para establecer una distancia máxima de búsqueda.
    - Después, se recuperan los planes que tienen coberturas en la lista filtrada de coberturas.
    - Finalmente, se serializa la lista de planes disponibles y se devuelve como respuesta HTTP.

    Nota:
    - Es necesario que las coberturas se almacenen en la base de datos con sus polígonos correctamente definidos para que la filtración funcione correctamente.
    """
    latitud = request.query_params.get("latitud")
    longitud = request.query_params.get("longitud")
    punto = Point(float(longitud), float(latitud))
    coberturas_punto = Cobertura.objects.filter(
        location__distance_lte=(punto, D(m=1000))
    )
    planes_disponibles = Plan.objects.filter(coberturas__in=coberturas_punto)
    serializer = PlanSerializer(planes_disponibles, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def crear_cobertura(request):
    """
    Vista para el endpoint de creación de cobertura.

    Permite a los usuarios crear una nueva cobertura con un polígono como ubicación.

    Parámetros:
    - request: La solicitud HTTP recibida.

    Retorna:
    - Una respuesta HTTP con los datos de la cobertura creada o los errores de validación.
    """
    data = request.data
    coordinates = data["location"]["coordinates"]
    poligono = GEOSGeometry(json.dumps({"type": "Polygon", "coordinates": coordinates}))
    data["location"] = poligono
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

    JSON de entrada esperado:
    {
        "nombre": string,
        "precio": float,
        "coberturas": [integer]
    }

    Retorna:
    - Una respuesta HTTP con los datos del plan creado o los errores de validación.
    """
    serializer = PlanSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
