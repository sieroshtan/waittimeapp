from rest_framework import permissions


class IsOwnObject(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj and obj.user_id == request.user.id
