from django import forms

class StudentForm(forms.Form):
    id = forms.IntegerField(required=False, widget=forms.HiddenInput())
    name = forms.CharField(max_length=100, label='الاسم الكامل')
    email = forms.EmailField(label='البريد الإلكتروني')
    phone = forms.CharField(max_length=20, label='رقم الهاتف')
    gpa = forms.FloatField(label='المعدل التراكمي')
    college = forms.CharField(max_length=100, label='الكلية')
    address = forms.CharField(max_length=200, label='العنوان')