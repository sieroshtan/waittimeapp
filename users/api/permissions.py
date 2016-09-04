from rest_framework import permissions


class IsCreationOrIsAuthenticated(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated():
            if view.action == 'create':
                return True
        return request.user and request.user.is_authenticated()


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj and obj.id == request.user.id
