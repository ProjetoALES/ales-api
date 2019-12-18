from django.shortcuts import get_object_or_404
from django.http import Http404

from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from rest_framework.response import Response

from .models import Semester
from .serializers import SemesterSerializer


class SemesterViewSet(viewsets.ViewSet):
    """
    Viewset for CRUD of semesters
    """

    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

    def get_object(self, pk):
        try:
            return Semester.objects.get(pk=pk)
        except Semester.DoesNotExist:
            raise Http404

    def list(self, request):
        queryset = Semester.objects.all()
        serializer = SemesterSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = SemesterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        semester = self.get_object(pk)
        if (semester):
            serializer = SemesterSerializer(semester)
            return Response(serializer.data)

    def put(self, request, pk, format=None):
        semester = self.get_object(pk)
        serializer = SemesterSerializer(semester, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        semester = self.get_object(pk)
        if (semester):
            semester.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
