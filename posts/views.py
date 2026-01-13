from rest_framework import viewsets, permissions
from .models import Post
from .serializers import PostSerializer


# ViewSet que maneja todas las operaciones CRUD para el modelo Nota
class PostViewSet(viewsets.ModelViewSet):
    # Solo se permiten GET para todos, pero las demás acciones requieren autenticación
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = PostSerializer

    # Esta función determina qué notas se pueden ver (Solo las del user logueado)
    def get_queryset(self):
        # Filtra el queryset para mostrar SÓLO las notas del user actualmente autenticado
        return Post.objects.filter(user=self.request.user)

    # Sobreescribe el método para crear el objeto.
    # Esto inyecta el user actual en el campo 'user' del modelo automáticamente.
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
