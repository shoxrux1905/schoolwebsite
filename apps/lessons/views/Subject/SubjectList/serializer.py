from rest_framework import serializers

from apps.lessons.models import Subject

class SubjectListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields ='__all__'