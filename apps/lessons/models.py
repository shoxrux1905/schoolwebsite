from django.db import models

from apps.common.models import BaseModel

class Subject(BaseModel) :
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
class Teacher(BaseModel) :
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone_number = models.CharField(max_length=20)
    pfp = models.ImageField(upload_to='students/pfps')
    subject = models.ManyToManyField(Subject)
    
    def __str__(self):
        return self.first_name
    
class Class(BaseModel) :
    name = models.CharField(max_length=200)
    capacity = models.PositiveSmallIntegerField(default=30)
    major = models.ForeignKey(Subject, models.SET_NULL, null=True, blank=True)
    curator = models.ForeignKey(Teacher, models.PROTECT, null=True)
    room_number = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return self.name
    
class Student(BaseModel) :
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone_number = models.CharField(max_length=20)
    pfp = models.ImageField(upload_to='students/pfps')
    klass = models.ForeignKey(Class, on_delete=models.SET_NULL, null = True)
    
    def __str__(self):
        return self.last_name