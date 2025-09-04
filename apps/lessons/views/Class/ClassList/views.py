from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from apps.lessons.models import Class
from apps.lessons.views.Class.ClassList.serializer import ClassListSerializer

def class_list_view(request) :
    classes = Class.objects.all()
    return render(request, 'class/class_list.html', {'classes': classes})

@api_view(['GET'])
def class_list_api_view(request) :
    classes = Class.objects.all()
    serializer = ClassListSerializer(classes, many=True)
    return Response(serializer.data)