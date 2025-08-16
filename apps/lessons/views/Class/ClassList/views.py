from django.shortcuts import render
from apps.lessons.models import Class

def class_list_view(request) :
    classes = Class.objects.all()
    return render(request, 'class/class_list.html', {'classes': classes})