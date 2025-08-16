from django.shortcuts import get_object_or_404, render, redirect
from apps.lessons.models import Teacher

def teacher_delete_view(request, pk):
    form = get_object_or_404(Teacher, pk=pk)
    if request.method == 'POST':
        form.delete()
        return redirect('teacher_list')
    return render(request, 'teacher/teacher_delete.html', {'form': form})