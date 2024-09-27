from django.contrib import admin
from django.contrib.auth import get_user_model
from core.models import Product
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.
class UserAdmin(BaseUserAdmin):
    """Define admin page for users."""

    ordering = ["id"]
    list_display = ["email", "name", "role"]
    fieldsets = [
        [None, {"fields": ["email", "password"]}],
        ["Permissions",
            {"fields": ["role", "is_staff", "is_superuser"]}],
        ["Important_dates", {"fields": ["last_login"]}]
    ]
    readonly_fields = ["last_login"]
    add_fieldsets = [
        [None, {
            "classes": ["wide"],
            "fields":[
                "email",
                "name",
                "password1",
                "password2",
                "is_superuser",
                "is_staff"
            ]
        }]
    ]


admin.site.register(get_user_model(), UserAdmin)
admin.site.register(Product)
