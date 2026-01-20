from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.http import HttpResponse
from django.conf.urls.static import static
from backend import settings


def health_check(request):
    return HttpResponse("OK", status=200)


urlpatterns = [
    path("admin/", admin.site.urls),
    # 1. Rutas de la API de Notas
    # path("api/", include("posts.urls")),
    # 2. Account API Routes
    path("api/account/", include("account.urls")),
    # 3. Rutas de Autenticación JWT (para React/Postman)
    # /api/token/ -> Obtener par de tokens (acceso y refresco)
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    # /api/token/refresh/ -> Refrescar el token de acceso
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # Opcional: Rutas para la interfaz de navegación de la API de DRF
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("health/", health_check, name="health_check"),
]


# Add this to serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
