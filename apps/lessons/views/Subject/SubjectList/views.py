from django.shortcuts import render
from apps.lessons.models import Subject

def subject_list_view(request) :
    subjects = Subject.objects.all()
    return render(request, 'subject/subject_list.html', context={'subjects': subjects})
    
