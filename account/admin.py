from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "company", "position"]
    list_filter = ["company"]
    search_fields = ["user__username", "user__email", "company", "position"]
