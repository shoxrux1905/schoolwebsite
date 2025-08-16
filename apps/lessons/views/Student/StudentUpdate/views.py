from django.shortcuts import get_object_or_404, render, redirect
from apps.lessons.models import Student
from apps.lessons.forms import StudentForm

def student_update_view(request, pk) :
    student = get_object_or_404(Student, pk=pk)
    form = StudentForm(instance=student)
    if request.method == 'POST' :
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid() :
            form.save()
            return redirect('student_list')
    return render(request, 'student/student_update.html', {'form': form})
