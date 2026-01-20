from django.urls import path
from .views import UserDetailView, UpdateUserView

app_name = "account"

urlpatterns = [
    path("me/", UserDetailView.as_view(), name="user-detail"),
    path("me/update/", UpdateUserView.as_view(), name="user-update"),
]
