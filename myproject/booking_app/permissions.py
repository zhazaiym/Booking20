from rest_framework.permissions import BasePermission

class CheckRolePermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.user_role == 'client':
            return True
        return False

class CreateRolePermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.user_role == 'owner':
            return True
        return False


