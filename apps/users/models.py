from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser) : 
    SHIFT_CHOICES = (
        ('MORNING_SHIFT', 'Morning shift'),
        ('DAY_SHIFT', 'Day shift'),
        ('NIGHT_SHIFT', 'Night shift'),
    )
    LANG_CHOICES = (
        ('UZBEK', 'Uzbek'),
        ('RUSSIAN', 'Russian'),
        ('ENGLISH', 'English'),
    )
    BLOOD_CHOICES = (
        ('A_POS', 'A+'),
        ('A_NEG', 'A-'),
        ('B_POS', 'B+'),
        ('B_NEG', 'B-'),
        ('AB_POS', 'AB+'),
        ('AB_NEG', 'AB-'),
        ('O_POS', 'O+'),
        ('O_NEG', 'O-'),
    )
    GENDER_CHOICES = (
        ('MALE', 'Male'),
        ('FEMALE', 'Female'),
    )
    
    qr_code = models.ImageField(upload_to='users/qr_codes/', blank=True, null=True)
    teacher_rating = models.CharField(max_length=500, blank=True, null=True)
    shift = models.CharField(max_length=20, choices=SHIFT_CHOICES, default=SHIFT_CHOICES[0][0])
    study_lang = models.CharField(max_length=20, choices=LANG_CHOICES, default=LANG_CHOICES[0][0])
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=500, blank=True, null=True)
    blood_group = models.CharField(max_length=500, choices=BLOOD_CHOICES, blank=True, null=True)
    date_of_birth = models.DateTimeField(blank=True, null=True)
    gender = models.CharField(error_messages=10, choices=GENDER_CHOICES, blank=True, null=True)
    pfp = models.ImageField(upload_to='users/images', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    