from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet

# Crea un router para generar automáticamente las URLs del ViewSet
router = DefaultRouter()
# SOLUCIÓN: Agregamos 'basename="notas"' para indicar el nombre base del recurso.
router.register(r"posts", PostViewSet, basename="posts")

urlpatterns = [
    path("", include(router.urls)),
]
