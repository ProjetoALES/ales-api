from rest_framework import serializers
from .models import Professor, Student

from django.contrib.auth.hashers import make_password


class ProfessorSerializer(serializers.ModelSerializer):

    def validate_password(self, value: str) -> str:
        return make_password(value)

    class Meta:
        model = Professor
        fields = ['id', 'name', 'email', 'phone', 'is_manager',
                  'gender', 'course', 'enroll_year', 'birthday', 'is_active', 'password']


class StudentSerializer(serializers.ModelSerializer):

    def validate_password(self, value: str) -> str:
        return make_password(value)

    class Meta:
        model = Student
        fields = ['id', 'name', 'email', 'phone', 'gender', 'birthday', 'document',
                  'authorization', 'address_code', 'locomotion', 'travel_time', 'lunch_at_school', 'password']
