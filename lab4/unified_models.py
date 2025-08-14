from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class College(models.Model):
    """نموذج يمثل الكلية في النظام الجامعي"""
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=10, unique=True)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name

class Department(models.Model):
    """نموذج يمثل القسم في النظام الجامعي"""
    college = models.ForeignKey(College, on_delete=models.CASCADE, related_name='departments')
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    
    def __str__(self):
        return f"{self.college.name} - {self.name}"

class Teacher(models.Model):
    """نموذج يمثل المعلم في النظام الجامعي"""
    employee_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='teachers')
    hire_date = models.DateField()
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.name} ({self.employee_id})"

class Student(models.Model):
    """نموذج يمثل الطالب في النظام الجامعي"""
    student_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    age = models.IntegerField(validators=[MinValueValidator(16), MaxValueValidator(40)])
    address = models.TextField()
    college = models.ForeignKey(College, on_delete=models.CASCADE, related_name='students')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='students')
    gpa = models.DecimalField(max_digits=3, decimal_places=2, validators=[MinValueValidator(0.0), MaxValueValidator(4.0)])
    enrollment_date = models.DateField()
    advisor = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True, related_name='advised_students')
    
    def __str__(self):
        return f"{self.name} ({self.student_id})"

class Course(models.Model):
    """نموذج يمثل المقرر الدراسي"""
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='courses')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='courses')
    credits = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(6)])
    max_students = models.IntegerField(default=50)
    
    def __str__(self):
        return f"{self.code} - {self.name}"

class Enrollment(models.Model):
    """نموذج يمثل تسجيل الطالب في مقرر"""
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='enrollments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments')
    enrollment_date = models.DateField(auto_now_add=True)
    grade = models.CharField(max_length=2, blank=True, null=True)
    
    class Meta:
        unique_together = ['student', 'course']
    
    def __str__(self):
        return f"{self.student.name} - {self.course.name}"
