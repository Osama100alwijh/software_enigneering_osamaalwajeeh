
# student/forms.py
# This file defines the forms for the Student and Teacher models.
# يستخدم هذا الملف ModelForm لإنشاء نماذج تلقائية من نماذج الطالب والمعلم.

from django import forms
from .models import Student, Teacher

class StudentForm(forms.ModelForm):
    """
    Form for creating and updating a Student model instance.
    نموذج لإنشاء وتحديث بيانات الطالب.
    """
    class Meta:
        model = Student
        fields = ['name', 'age', 'address', 'phone', 'email', 'college', 'gpa']
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'أدخل الاسم الكامل للطالب'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'أدخل عمر الطالب', 'min': 16, 'max': 40}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'أدخل عنوان السكن'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'أدخل رقم الهاتف'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'أدخل البريد الإلكتروني'}),
            'college': forms.Select(attrs={'class': 'form-select'}),
            'gpa': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'placeholder': 'أدخل المعدل التراكمي'}),
        }
        
        labels = {
            'name': 'الاسم الكامل',
            'age': 'العمر',
            'address': 'العنوان',
            'phone': 'رقم الهاتف',
            'email': 'البريد الإلكتروني',
            'college': 'الكلية',
            'gpa': 'المعدل التراكمي',
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['college'].choices = [
            ('', 'اختر الكلية'),
            ('الحاسبات', 'كلية الحاسبات'),
            ('الهندسة', 'كلية الهندسة'),
            ('الطب', 'كلية الطب'),
            ('الصيدلة', 'كلية الصيدلة'),
        ]

class TeacherForm(forms.ModelForm):
    """
    Form for creating and updating a Teacher model instance.
    نموذج لإنشاء وتحديث بيانات المعلم.
    """
    class Meta:
        model = Teacher
        fields = ['name', 'age', 'phone', 'email', 'department', 'hired_date']
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'أدخل الاسم الكامل للمعلم'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'أدخل عمر المعلم', 'min': 22, 'max': 65}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'أدخل رقم الهاتف'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'أدخل البريد الإلكتروني'}),
            'department': forms.Select(attrs={'class': 'form-select'}),
            'hired_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
        
        labels = {
            'name': 'الاسم الكامل',
            'age': 'العمر',
            'phone': 'رقم الهاتف',
            'email': 'البريد الإلكتروني',
            'department': 'القسم',
            'hired_date': 'تاريخ التعيين',
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['department'].choices = [
            ('', 'اختر القسم'),
            ('هندسة البرمجيات', 'قسم هندسة البرمجيات'),
            ('علوم الحاسب', 'قسم علوم الحاسب'),
            ('نظم المعلومات', 'قسم نظم المعلومات'),
        ]


# # students_app/forms.py
# from django import forms
# from .models import Student

# class StudentForm(forms.ModelForm):
#     class Meta:
#         model = Student
#         fields = ['name', 'age', 'address', 'phone', 'email', 'college', 'gpa', 'photo']
#         widgets = {
#             'name': forms.TextInput(attrs={'class': 'form-control'}),
#             'age': forms.NumberInput(attrs={'class': 'form-control'}),
#             'address': forms.TextInput(attrs={'class': 'form-control'}),
#             'phone': forms.TextInput(attrs={'class': 'form-control'}),
#             'email': forms.EmailInput(attrs={'class': 'form-control'}),
#             'college': forms.TextInput(attrs={'class': 'form-control'}),
#             'gpa': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1', 'min': '0.0', 'max': '4.0'}),
#             'photo': forms.FileInput(attrs={'class': 'form-control'}),
#         }
#         labels = {
#             'name': 'الاسم',
#             'age': 'العمر',
#             'address': 'العنوان',
#             'phone': 'رقم الهاتف',
#             'email': 'البريد الإلكتروني',
#             'college': 'الكلية',
#             'gpa': 'المعدل التراكمي (GPA)',
#             'photo': 'صورة الطالب',
#         }