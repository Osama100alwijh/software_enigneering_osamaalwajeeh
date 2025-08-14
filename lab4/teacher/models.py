# teacher_app/models.py
# This file defines the database model for the Teacher.
# يتم تعريف نموذج قاعدة البيانات للمعلم في هذا الملف.

from django.db import models

class Teacher(models.Model):
    """
    Model for a teacher in the university system.
    نموذج يمثل المعلم في النظام الجامعي.
    """
    # The teacher's full name.
    # الاسم الكامل للمعلم.
    name = models.CharField(max_length=100)
    
    # The teacher's subject.
    # المادة التي يدرسها المعلم.
    subject = models.CharField(max_length=100)
    
    # The teacher's email address, must be unique.
    # البريد الإلكتروني للمعلم، يجب أن يكون فريدًا.
    email = models.EmailField(unique=True)

    # The teacher's phone number.
    # رقم هاتف المعلم.
    phone = models.CharField(max_length=15, blank=True, null=True)
    
    class Meta:
        # Define the default table name for the model
        # تحديد اسم الجدول الافتراضي للنموذج
        db_table = 'teachers'

    def __str__(self):
        return self.name

