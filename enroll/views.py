from django.http import Http404

from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .models import Professor, Student
from .serializers import ProfessorSerializer, StudentSerializer
from .permissions import IsProfessor, IsStudent, OwnProfile


class ProfessorViewSet(viewsets.ViewSet):
    """
    Viewset for CRUD of Professors
    """

    def get_permissions(self):
        if self.action == 'delete':
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [IsAdminUser | (IsProfessor & OwnProfile)]
        return [permission() for permission in permission_classes]

    def get_object(self, pk):
        try:
            return Professor.objects.get(pk=pk)
        except Professor.DoesNotExist:
            raise Http404

    def list(self, request):
        queryset = Professor.objects.all()
        serializer = ProfessorSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, format=None):
        serializer = ProfessorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        professor = self.get_object(pk)
        if (professor):
            serializer = ProfessorSerializer(professor)
            return Response(serializer.data)

    def put(self, request, pk, format=None):
        professor = self.get_object(pk)
        serializer = ProfessorSerializer(professor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        professor = self.get_object(pk)
        if (professor):
            professor.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


class StudentViewSet(viewsets.ViewSet):
    """
    Viewset for CRUD of Students
    """

    def get_permissions(self):
        if self.action == 'delete':
            permission_classes = [IsAdminUser]
        elif self.action == 'create' or self.action == 'list':
            permission_classes = [IsAdminUser | IsProfessor]
        else:
            permission_classes = [IsAdminUser | (
                IsStudent & OwnProfile) | IsProfessor]
        return [permission() for permission in permission_classes]

    def list(self, request):
        queryset = Student.objects.all()
        serializer = StudentSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
