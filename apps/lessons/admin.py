from django.contrib import admin

from apps.lessons.models import Class, Student, Subject, Teacher

admin.site.register(Subject)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Class)
