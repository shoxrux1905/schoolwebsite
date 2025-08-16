from django.shortcuts import render
from apps.lessons.models import Student

def student_list_view(request):
    students = Student.objects.all()
    return render(request, 'student/student_list.html', {'students': students})