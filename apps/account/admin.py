from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "is_active")
    sortable_by = ("id", "username")
    list_editable = ("is_active",)
    search_fields = ("username",)
    