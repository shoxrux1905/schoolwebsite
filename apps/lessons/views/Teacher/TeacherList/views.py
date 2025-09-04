from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from apps.lessons.models import Teacher
from apps.lessons.views.Teacher.TeacherList.serializer import TeacherListSerializer

def teacher_list_view(request) :
    teachers = Teacher.objects.all()
    return render(request, 'teacher/teacher_list.html', context={'teachers':teachers})

@api_view(['GET'])
def teacher_list_api_view(request):
    teachers = Teacher.objects.all()
    serializer = TeacherListSerializer(teachers, many=True)
    return Response(serializer.data)