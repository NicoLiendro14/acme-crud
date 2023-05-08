from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User


class RegisterViewTestCase(APITestCase):
    def test_register_user(self):
        url = reverse("register")
        data = {"username": "testuser", "password": "testpassword"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("token", response.data)


class LoginViewTestCase(APITestCase):
    def setUp(self):
        self.username = "testuser"
        self.password = "testpassword"
        self.user = User.objects.create_user(
            username=self.username, password=self.password
        )

    def test_login(self):
        url = reverse("login")
        data = {"username": self.username, "password": self.password}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("token", response.data)


class ObtenerPlanesDisponiblesTestCase(APITestCase):
    def test_obtener_planes_disponibles(self):
        url = reverse("obtener_planes_disponibles")
        latitud = 0.0
        longitud = 0.0
        response = self.client.get(url, {"latitud": latitud, "longitud": longitud})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        # Asegúrate de verificar los resultados esperados en la respuesta
