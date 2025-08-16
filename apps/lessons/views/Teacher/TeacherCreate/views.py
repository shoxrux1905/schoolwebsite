from django.shortcuts import render, redirect
from apps.lessons.forms import TeacherForm

def teacher_create_view(request) :
    form = TeacherForm()
    if request.method == 'POST':
        form = TeacherForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('teacher_list')
    return render(request, 'teacher/teacher_create.html', {'form': form})
        