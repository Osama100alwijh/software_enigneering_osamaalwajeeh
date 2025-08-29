# teacher/forms.py
# Define the form for the Teacher model here.

from django import forms
from .models import Teacher

class TeacherForm(forms.ModelForm):
    """
    Form for creating and updating a Teacher model instance.
    نموذج لإنشاء وتحديث بيانات المعلم.
    """
    class Meta:
        model = Teacher
        fields = ['name', 'subject', 'email']
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'أدخل الاسم الكامل للمعلم'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'أدخل المادة التي يدرسها'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'أدخل البريد الإلكتروني'}),
        }
        
        labels = {
            'name': 'الاسم الكامل',
            'subject': 'المادة',
            'email': 'البريد الإلكتروني',
        }

