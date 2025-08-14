# teacher_app/urls.py
# This file includes the URL patterns for the teacher management system.
# يتضمن هذا الملف أنماط URL لنظام إدارة المعلمين.

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='teacher_home'),
    path('all_teachers/', views.all_teachers, name='all_teachers'),
    path('add_teacher/', views.add_teacher, name='add_teacher'),
    path('show_teacher_search/', views.show_teacher_search, name='show_teacher_search'),
    path('show_teacher/<int:teacher_id>/', views.show_teacher, name='show_teacher'),
    path('edit_teacher_search/', views.edit_teacher_search, name='edit_teacher_search'),
    path('edit_teacher/<int:teacher_id>/', views.edit_teacher, name='edit_teacher'),
    path('delete_teacher_search/', views.delete_teacher_search, name='delete_teacher_search'),
    path('delete_teacher/<int:teacher_id>/', views.delete_teacher, name='delete_teacher'),
    path('settings/', views.system_settings, name='teacher_settings'),
    path('dashboard/', views.dashboard, name='teacher_dashboard'),
]
