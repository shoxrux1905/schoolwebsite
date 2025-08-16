from django.shortcuts import get_object_or_404, redirect, render
from apps.lessons.forms import ClassForm
from apps.lessons.models import Class

def class_update_view(request, pk) :
    classes = get_object_or_404(Class, pk=pk)
    form = ClassForm(instance=classes)
    if request.method == 'POST':
        form = ClassForm(request.POST, instance=classes)
        if form.is_valid() :
            form.save()
            return redirect('class_list')
    return render(request, 'class/class_update.html', {'form': form})