from django.urls import path

from apps.lessons.views import subject_create_view, subject_list_view, subject_update_view, subject_delete_view

from apps.lessons.views.Teacher.TeacherCreate.views import teacher_create_view
from apps.lessons.views.Teacher.TeacherDelete.views import teacher_delete_view
from apps.lessons.views.Teacher.TeacherList.views import teacher_list_view
from apps.lessons.views.Teacher.TeacherUpdate.views import teacher_update_view

from apps.lessons.views.Class.ClassList.views import class_list_view
from apps.lessons.views.Class.ClassCreate.views import class_create_view
from apps.lessons.views.Class.ClassUpdate.views import class_update_view
from apps.lessons.views.Class.ClassDelete.views import class_delete_view

from apps.lessons.views.Student.StudentList.views import student_list_view
from apps.lessons.views.Student.StudentCreate.views import student_create_view
from apps.lessons.views.Student.StudentUpdate.views import student_update_view
from apps.lessons.views.Student.StudentDelete.views import student_delete_view

urlpatterns = [
    path('subjects/', subject_list_view, name='subject_list'),
    path('subjects/add/', subject_create_view, name='subject_create'),
    path('subjects/edit/<int:pk>/', subject_update_view, name='subject_update'),
    path('subjects/delete/<int:pk>/', subject_delete_view, name='subject_delete'),
    
    path('teachers/', teacher_list_view, name='teacher_list'),
    path('teachers/add/', teacher_create_view, name='teacher_create'),
    path('teachers/edit/<int:pk>/', teacher_update_view, name='teacher_update'),
    path('teachers/delete/<int:pk>/', teacher_delete_view, name='teacher_delete'),  
    
    path('classes/', class_list_view, name='class_list'),
    path('classes/add/', class_create_view, name='class_create'),
    path('classes/edit/<int:pk>/', class_update_view, name='class_update'),
    path('classes/delete/<int:pk>/', class_delete_view, name='class_delete'),
    
    path('students/', student_list_view, name='student_list'),
    path('students/add/', student_create_view, name='student_create'),
    path('students/edit/<int:pk>/', student_update_view, name='student_update'),
    path('students/delete/<int:pk>/', student_delete_view, name='student_delete'),
]
