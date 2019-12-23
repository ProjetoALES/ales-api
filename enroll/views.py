from django.http import Http404
from django.core.mail import send_mail
from django.template.loader import render_to_string


from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .models import Professor, Student
from .serializers import ProfessorSerializer, StudentSerializer
from .permissions import IsProfessor, IsStudent
from api import settings


class ProfessorViewSet(viewsets.ViewSet):
    """
    Viewset for CRUD of Professors
    """

    def get_permissions(self):
        if self.action == 'destroy':
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [IsAdminUser | IsProfessor]
        return [permission() for permission in permission_classes]

    def get_object(self, pk):
        try:
            return Professor.objects.get(pk=pk)
        except Professor.DoesNotExist:
            raise Http404

    def send_account_created_email(self, title, sender, receiver_email, html_message, msg=''):
        send_mail(title, msg, sender, [
                  receiver_email], html_message=html_message)

    def list(self, request):
        queryset = Professor.objects.all()
        serializer = ProfessorSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, format=None):
        serializer = ProfessorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            html_message = render_to_string(
                'email/account_created.html', {'protocol': settings.PROTOCOL, 'domain': settings.DOMAIN, 'url': 'login'})
            self.send_account_created_email(
                "Projeto Ales - Conta Criada", settings.EMAIL_HOST_USER, serializer.data['email'], html_message)
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

    def destroy(self, request, pk, format=None):
        professor = self.get_object(pk)
        if (professor):
            professor.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


class StudentViewSet(viewsets.ViewSet):
    """
    Viewset for CRUD of Students
    """

    def get_permissions(self):
        if self.action == 'destroy':
            permission_classes = [IsAdminUser]
        elif self.action == 'create' or self.action == 'list':
            permission_classes = [IsAdminUser | IsProfessor]
        else:
            permission_classes = [IsAdminUser | IsStudent | IsProfessor]
        return [permission() for permission in permission_classes]

    def get_object(self, pk):
        try:
            return Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            raise Http404

    def send_account_created_email(self, title, sender, receiver_email, html_message, msg=''):
        send_mail(title, msg, sender, [
                  receiver_email], html_message=html_message)

    def list(self, request):
        queryset = Student.objects.all()
        serializer = StudentSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            html_message = render_to_string(
                'email/account_created.html', {'protocol': settings.PROTOCOL, 'domain': settings.DOMAIN, 'url': 'login'})
            self.send_account_created_email(
                "Projeto Ales - Conta Criada", settings.EMAIL_HOST_USER, serializer.data['email'], html_message)
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        student = self.get_object(pk)
        if (student):
            serializer = StudentSerializer(student)
            return Response(serializer.data)

    def put(self, request, pk, format=None):
        student = self.get_object(pk)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk, format=None):
        student = self.get_object(pk)
        if (student):
            student.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
