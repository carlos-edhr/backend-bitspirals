from django.contrib import admin
from .models import Post

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["tittle", "content", "created_at", "updated_at", "user"]
    list_filter = ["created_at"]
