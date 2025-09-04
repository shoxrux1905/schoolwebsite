from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from apps.lessons.models import Subject
from apps.lessons.views.Subject.SubjectList.serializer import SubjectListSerializer

def subject_list_view(request) :
    subjects = Subject.objects.all()
    return render(request, 'subject/subject_list.html', context={'subjects': subjects})
    
@api_view(['GET'])
def subject_list_api_view(request) :
    subjects = Subject.objects.all()
    serializer = SubjectListSerializer(subjects, many=True)
    return Response(serializer.data)