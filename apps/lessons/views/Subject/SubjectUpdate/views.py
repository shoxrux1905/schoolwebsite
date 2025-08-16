from django.shortcuts import get_object_or_404, render, redirect
from apps.lessons.forms import SubjectForm
from apps.lessons.models import Subject

def subject_update_view(request, pk) :
    subject = get_object_or_404(Subject, pk=pk)
    form = SubjectForm(instance = subject)
    if request.method == 'POST' :
        form = SubjectForm(request.POST, instance=subject)
        if form.is_valid() :
            form.save()
        return redirect('subject_list')
    return render(request, 'subject/subject_update.html', {'form' : form})