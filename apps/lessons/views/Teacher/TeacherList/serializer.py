from rest_framework import serializers

from apps.lessons.models import Teacher

class TeacherListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'