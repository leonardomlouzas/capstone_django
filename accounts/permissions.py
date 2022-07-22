from rest_framework.permissions import BasePermission
from rest_framework.request import Request

from .models import Account


class IsAdmin(BasePermission):
    def has_object_permission(self, request: Request, _, obj: Account):
        if request.user.is_superuser:
            return True

        return obj == request.user
