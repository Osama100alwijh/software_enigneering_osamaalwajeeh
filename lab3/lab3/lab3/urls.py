# In lab3/urls.py
# This file includes the URLs from the students and teachers apps.
# يتضمن هذا الملف عناوين URL من تطبيقي الطلاب والمعلمين.

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('student.urls')),
    # path('', include('teacher.urls')),  # Add the teacher app URLs
]
