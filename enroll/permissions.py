from rest_framework import permissions


class IsProfessor(permissions.BasePermission):
    def has_permission(self, request, view):
        if (request.user and request.user.is_authenticated):
            return request.user.is_professor
        return False


class IsStudent(permissions.BasePermission):
    def has_permission(self, request, view):
        if (request.user and request.user.is_authenticated):
            return request.user.is_student
        return False
