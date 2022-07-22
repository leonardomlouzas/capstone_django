from rest_framework import permissions
from rest_framework.request import Request


class IsAdminOrReadOnlyBook(permissions.BasePermission):
    def has_permission(self, request: Request, _):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.is_superuser


class IsAdminOrReadOnlyAccount(permissions.BasePermission):
    def has_permission(self, request: Request, _):
        if request.method in permissions.SAFE_METHODS:
            return request.user.is_superuser

        return True
