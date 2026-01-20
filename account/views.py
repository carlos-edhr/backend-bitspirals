from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import RetrieveAPIView, UpdateAPIView
from django.contrib.auth import get_user_model
from .serializers import UserSerializer, UpdateUserSerializer, UpdateProfileSerializer

User = get_user_model()


class UserDetailView(RetrieveAPIView):
    """
    Get current user details including profile
    """

    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class UpdateUserView(UpdateAPIView):
    """
    Update user information
    """

    permission_classes = [IsAuthenticated]
    serializer_class = UpdateUserSerializer

    def get_object(self):
        return self.request.user

    def update(self, request, *args, **kwargs):
        user = self.get_object()
        user_data = {}
        profile_data = {}

        # Handle file uploads separately
        files = request.FILES

        # If there's a photo in files
        if "photo" in files:
            profile_data["photo"] = files["photo"]

        # Parse request data (excluding files)
        for key, value in request.data.items():
            if key == "profile":
                if isinstance(value, dict):
                    profile_data.update(value)
            elif key.startswith("profile."):
                profile_field = key.split(".")[1]
                profile_data[profile_field] = value
            elif key in UpdateUserSerializer.Meta.fields:
                user_data[key] = value
            elif (
                key == "photo" and value == ""
            ):  # Handle empty string for photo removal
                profile_data["photo"] = None  # Set to None to remove photo
            elif key != "photo":  # Skip photo as we handled it from files
                profile_data[key] = value

        # Update user
        user_serializer = self.get_serializer(user, data=user_data, partial=True)

        if user_serializer.is_valid():
            user_serializer.save()

            # Update profile if profile data is provided
            if (profile_data or files) and hasattr(user, "profile"):
                # If there's a photo file but not in profile_data, add it
                if "photo" in files and "photo" not in profile_data:
                    profile_data["photo"] = files["photo"]

                profile_serializer = UpdateProfileSerializer(
                    user.profile, data=profile_data, partial=True
                )
                if profile_serializer.is_valid():
                    profile_serializer.save()
                else:
                    return Response(
                        profile_serializer.errors, status=status.HTTP_400_BAD_REQUEST
                    )

            # Return complete user data
            return Response(
                UserSerializer(user, context=self.get_serializer_context()).data,
                status=status.HTTP_200_OK,
            )

        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
