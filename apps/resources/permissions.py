from rest_framework import permissions

class AuthorSuperOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Check if the authenticated user is a superuser
        if request.user.is_superuser:
            return True

        # Check if the request method is a safe method
        if request.method in permissions.SAFE_METHODS:
            return True

        # Check if the authenticated user is the owner of the resource
        if request.user.id == obj.user_id.id:
            return True

        return False
