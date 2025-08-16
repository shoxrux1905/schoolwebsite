from django.shortcuts import render
from apps.lessons.models import Teacher

def teacher_list_view(request) :
    teachers = Teacher.objects.all()
    return render(request, 'teacher/teacher_list.html', context={'teachers':teachers})