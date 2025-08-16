from django.shortcuts import get_object_or_404, render, redirect
from apps.lessons.models import Class

def class_delete_view(request, pk) :
    classes = get_object_or_404(Class, pk=pk)
    if request.method == 'POST':
        classes.delete()
        return redirect('class_list')
    return render(request, 'class/class_delete.html', {'classes': classes})