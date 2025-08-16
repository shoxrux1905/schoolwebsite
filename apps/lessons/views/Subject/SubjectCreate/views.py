from django.shortcuts import redirect, render
from apps.lessons.forms import SubjectForm

def subject_create_view(request) :
    form = SubjectForm()
    if request.method == 'POST' :
        form = SubjectForm(request.POST)
        if form.is_valid() :
            form.save()
            return redirect('subject_list')
    return render(request, 'subject/subject_create.html', {'form': form})