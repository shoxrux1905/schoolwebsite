from django.shortcuts import get_object_or_404, redirect, render
from apps.lessons.models import Student

def student_delete_view(request, pk) :
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST' :
        student.delete()
        return redirect('student_list')
    return render(request, 'student/student_delete.html', {'student': student})