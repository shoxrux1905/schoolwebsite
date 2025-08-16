from django import forms

from .models import Subject, Teacher, Student, Class

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['name']

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'pfp', 'subject']
        
class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ['name', 'capacity', 'major', 'curator', 'room_number']
        
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'pfp', 'klass']