from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    # El campo es de solo lectura y obtendrá el nombre de user del objeto
    user_username = serializers.ReadOnlyField(source="user.username")

    class Meta:
        model = Post
        # Campos que se envían y reciben en la API
        fields = [
            "id",
            "tittle",
            "content",
            "created_at",
            "updated_at",
            "user",
            "user_username",
        ]
        # Los campos 'user' y 'user_username' no pueden ser modificados por el cliente
        read_only_fields = ["user", "user_username"]
