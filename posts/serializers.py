from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    # El campo es de solo lectura y obtendrá el nombre de usuario del objeto
    usuario_username = serializers.ReadOnlyField(source="usuario.username")

    class Meta:
        model = Post
        # Campos que se envían y reciben en la API
        fields = [
            "id",
            "title",
            "content",
            "created_at",
            "updated_at",
            "user",
            "user_username",
        ]
        # Los campos 'usuario' y 'usuario_username' no pueden ser modificados por el cliente
        read_only_fields = ["user", "user_username"]
