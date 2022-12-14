from rest_framework import permissions

class IfIsOwner(permissions.BasePermission):
    def has_object_permission_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user