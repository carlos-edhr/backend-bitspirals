from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    # 1. Rutas de la API de Notas
    path("api/", include("posts.urls")),
    # 2. Rutas de Autenticación JWT (para React/Postman)
    # /api/token/ -> Obtener par de tokens (acceso y refresco)
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    # /api/token/refresh/ -> Refrescar el token de acceso
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # Opcional: Rutas para la interfaz de navegación de la API de DRF
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
