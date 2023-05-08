"""postgis_multifiber URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import (
    CoberturaList,
    registrar_usuario,
    crear_cobertura,
    crear_plan,
    obtener_planes_disponibles,
)
from app.views import LoginView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("registrar-usuario/", registrar_usuario, name="registrar_usuario"),
    path("crear-cobertura/", crear_cobertura, name="crear_cobertura"),
    path("crear-plan/", crear_plan, name="crear_plan"),
    path(
        "obtener-planes-disponibles/",
        obtener_planes_disponibles,
        name="obtener_planes_disponibles",
    ),
    path("coberturas/", CoberturaList.as_view(), name="cobertura-list"),
    path("login/", LoginView.as_view(), name="login"),
]
