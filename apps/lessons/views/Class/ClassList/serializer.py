from rest_framework import serializers

from apps.lessons.models import Class

class ClassListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = '__all__'