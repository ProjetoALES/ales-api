from rest_framework import permissions


class IsProfessor(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_professor


class IsStudent(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_student


class OwnProfile(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
