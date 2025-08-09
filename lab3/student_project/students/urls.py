# students/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # الرئيسية
    path('', views.home, name='home'),
    
    # الطلاب
    path('students/', views.all_students, name='all_students'),
    path('students/add/', views.add_student, name='add_student'),
    path('students/edit/<int:student_id>/', views.edit_student, name='edit_student'),
    path('students/delete/<int:student_id>/', views.delete_student, name='delete_student'),
    path('students/show/', views.show_student_search, name='show_student_search'),
    
    # لوحة التحكم والإعدادات
    path('dashboard/', views.dashboard, name='dashboard'),
    path('settings/', views.settings, name='settings'),
    
    # روابط البحث والتعديل والحذف
    path('edit-student-search/', views.edit_student_search, name='edit_student_search'),
    path('delete-student-search/', views.delete_student_search, name='delete_student_search'),
    path('show-student-data/<int:student_id>/', views.show_student_data, name='show_student_data'),

]
