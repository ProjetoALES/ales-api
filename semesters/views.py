from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.response import Response

from .models import Semester
from .serializers import SemesterSerializer


class SemesterViewSet(viewsets.ViewSet):
    """
    Viewset for list, create, delete and view (detail) semesters
    """

    def list(self, request):
        queryset = Semester.objects.all()
        serializer = SemesterSerializer(queryset, many=True)
        return Response(serializer.data)

    # def create()

    def retrieve(self, request, pk=None):
        queryset = Semester.objects.all()
        semester = get_object_or_404(queryset, pk=pk)
        serializer = SemesterSerializer(semester)
        return Response(serializer.data)

    # def update()

    # def destroy()
