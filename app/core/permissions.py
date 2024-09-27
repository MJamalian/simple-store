from rest_framework.permissions import BasePermission

from django.contrib.auth import get_user_model

manager_or_assistant = [get_user_model().UserRole.MANAGER, get_user_model().UserRole.ASSISTANT]


class IsManagerOrAssistant(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.role in manager_or_assistant)

class IsCustomer(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.role == get_user_model().UserRole.CUSTOMER)