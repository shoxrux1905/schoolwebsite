from django.urls import path

from apps.lessons.views import subject_create_view, subject_list_view, subject_update_view, subject_delete_view, subject_list_api_view
from apps.lessons.views import teacher_create_view, teacher_list_view, teacher_update_view, teacher_delete_view, teacher_list_api_view
from apps.lessons.views import class_create_view, class_list_view, class_update_view, class_delete_view, class_list_api_view
from apps.lessons.views import student_create_view, student_list_view, student_update_view, student_delete_view, student_list_api_view

urlpatterns = [
    path('subjects/', subject_list_view, name='subject_list'),
    path('subjects/add/', subject_create_view, name='subject_create'),
    path('subjects/edit/<int:pk>/', subject_update_view, name='subject_update'),
    path('subjects/delete/<int:pk>/', subject_delete_view, name='subject_delete'),
    path('subjects/api/list', subject_list_api_view, name='subject_api_list'),
    
    path('teachers/', teacher_list_view, name='teacher_list'),
    path('teachers/add/', teacher_create_view, name='teacher_create'),
    path('teachers/edit/<int:pk>/', teacher_update_view, name='teacher_update'),
    path('teachers/delete/<int:pk>/', teacher_delete_view, name='teacher_delete'),  
    path('teachers/api/list', teacher_list_api_view, name='teacher_api_list'),
    
    path('classes/', class_list_view, name='class_list'),
    path('classes/add/', class_create_view, name='class_create'),
    path('classes/edit/<int:pk>/', class_update_view, name='class_update'),
    path('classes/delete/<int:pk>/', class_delete_view, name='class_delete'),
    path('classes/api/list', class_list_api_view, name='class_api_list'),
    
    path('students/', student_list_view, name='student_list'),
    path('students/add/', student_create_view, name='student_create'),
    path('students/edit/<int:pk>/', student_update_view, name='student_update'),
    path('students/delete/<int:pk>/', student_delete_view, name='student_delete'),
    path('students/api/list', student_list_api_view, name='student_api_list'),
]
