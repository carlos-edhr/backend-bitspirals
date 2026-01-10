from rest_framework import viewsets, permissions
from .models import Post
from .serializers import PostSerializer


# ViewSet que maneja todas las operaciones CRUD para el modelo Nota
class PostViewSet(viewsets.ModelViewSet):
    # Solo se permiten GET para todos, pero las demás acciones requieren autenticación
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = PostSerializer

    # Esta función determina qué notas se pueden ver (Solo las del usuario logueado)
    def get_queryset(self):
        # Filtra el queryset para mostrar SÓLO las notas del usuario actualmente autenticado
        return Post.objects.filter(usuario=self.request.user)

    # Sobreescribe el método para crear el objeto.
    # Esto inyecta el usuario actual en el campo 'usuario' del modelo automáticamente.
    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)
