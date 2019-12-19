from rest_framework import serializers
from .models import Professor

from django.contrib.auth.hashers import make_password


class ProfessorSerializer(serializers.ModelSerializer):

    def validate_password(self, value: str) -> str:
        return make_password(value)

    class Meta:
        model = Professor
        fields = ['id', 'name', 'email', 'phone', 'is_manager',
                  'gender', 'course', 'enroll_year', 'age', 'is_active', 'password']
