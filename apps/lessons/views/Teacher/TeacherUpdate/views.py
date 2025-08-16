from django.shortcuts import render, redirect, get_object_or_404
from apps.lessons.models import Teacher
from apps.lessons.forms import TeacherForm

def teacher_update_view(request, pk) :
    teacher = get_object_or_404(Teacher, pk=pk)
    form = TeacherForm(instance=teacher)
    if request.method == 'POST':
        form = TeacherForm(request.POST, request.FILES, instance=teacher)
        if form.is_valid() :
            form.save()
            return redirect('teacher_list')
    return render(request, 'teacher/teacher_update.html', {'form': form})