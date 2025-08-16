from django.shortcuts import render, redirect
from apps.lessons.forms import ClassForm

def class_create_view(request) :
    form = ClassForm()
    if request.method == 'POST' :
        form = ClassForm(request.POST, request.FILES)
        if form.is_valid() :
            form.save()
            return redirect('class_list')
    return render(request, 'class/class_create.html', {'form': form})