from rest_framework import serializers

from apps.lessons.models import Student

class StudentListSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Student
        fields = '__all__'