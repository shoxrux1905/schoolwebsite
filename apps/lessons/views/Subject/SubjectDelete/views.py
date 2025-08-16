from django.shortcuts import render, redirect, get_object_or_404
from apps.lessons.models import Subject

def subject_delete_view(request, pk) :
    subject = get_object_or_404(Subject, pk=pk)
    if request.method == 'POST' :
        subject.delete()
        return redirect('subject_list')
    return render(request, 'subject/subject_delete.html', {'subject': subject})