from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Profile

User = get_user_model()


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            "company",
            "position",
            "date_of_birth",
            "photo",
            "updated_at",
        ]
        read_only_fields = ["updated_at"]


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "is_active",
            "date_joined",
            "profile",
        ]
        read_only_fields = ["id", "date_joined", "is_active"]


class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]


class UpdateProfileSerializer(serializers.ModelSerializer):
    photo = serializers.ImageField(required=False, allow_null=True)  # Add this

    class Meta:
        model = Profile
        fields = ["company", "position", "date_of_birth", "photo"]
