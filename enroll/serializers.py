from rest_framework import serializers
from .models import Professor


class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = ['name', 'email', 'phone', 'is_manager',
                  'gender', 'course', 'enroll_year', 'age']
