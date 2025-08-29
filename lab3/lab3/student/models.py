# student/models.py
# This file defines the database models for Student and Teacher.
# يتم تعريف نماذج قاعدة البيانات للطالب والمعلم في هذا الملف.

from django.db import models

class Student(models.Model):
    """
    Model for a student in the university system.
    نموذج يمثل الطالب في النظام الجامعي.
    """
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(unique=True)
    college = models.CharField(max_length=100)
    gpa = models.DecimalField(max_digits=3, decimal_places=2)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    """
    Model for a teacher in the university system.
    نموذج يمثل المعلم في النظام الجامعي.
    """
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    phone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=100)
    hired_date = models.DateField()

    def __str__(self):
        return self.name



# from django.db import models
# from django.core.validators import MinValueValidator

# class Student(models.Model):
#     name = models.CharField(max_length=100)
#     age = models.IntegerField(validators=[MinValueValidator(0)])
#     address = models.CharField(max_length=255)
#     phone = models.CharField(max_length=15, unique=True)
#     email = models.EmailField(unique=True)
#     college = models.CharField(max_length=100)
#     gpa = models.FloatField(validators=[MinValueValidator(0.0)])
#     photo = models.ImageField(upload_to='students/', null=True, blank=True)

#     def __str__(self):
#         return self.name