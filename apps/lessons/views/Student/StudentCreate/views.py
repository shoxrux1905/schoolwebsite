from django.shortcuts import render, redirect
from apps.lessons.forms import StudentForm

def student_create_view(request) :
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid() :
            form.save()
            return redirect('student_list')
    return render(request, 'student/student_create.html', {'form': form})
        