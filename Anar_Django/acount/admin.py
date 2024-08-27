from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User


class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ("email", "is_staff", "is_active",)
    list_filter = ("email", "is_staff", "is_active",)
    list_editable = ("is_staff", "is_active")
    fieldsets = (
        (None, {"fields": ("email","first_name","last_name", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        ("Əsas", {
            "classes": ("wide",),
            "fields": (
                "email","first_name","last_name", "password1", "password2",
            )}
        ),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")})
    )
    search_fields = ("email",)
    ordering = ("email",)


admin.site.register(User, CustomUserAdmin)