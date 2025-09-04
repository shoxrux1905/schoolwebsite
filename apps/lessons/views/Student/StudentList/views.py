from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from apps.lessons.models import Student
from apps.lessons.views.Student.StudentList.serializer import StudentListSerializer

def student_list_view(request):
    students = Student.objects.all()
    return render(request, 'student/student_list.html', {'students': students})

@api_view(['GET'])
def student_list_api_view(request):
    students = Student.objects.all()
    serializer = StudentListSerializer(students, many=True)
    return Response(serializer.data)