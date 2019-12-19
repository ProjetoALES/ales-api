from django.http import Http404

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from .models import Professor
from .serializers import ProfessorSerializer


class ProfessorViewSet(viewsets.ViewSet):
    """
    Viewset for CRUD of Professors
    """

    def get_object(self, pk):
        try:
            return Professor.objects.get(pk=pk)
        except Professor.DoesNotExist:
            raise Http404

    def list(self, request):
        queryset = Professor.objects.all()
        serializer = ProfessorSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ProfessorSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
