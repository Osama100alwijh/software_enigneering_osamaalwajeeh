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