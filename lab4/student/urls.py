from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('all_students/', views.all_students, name='all_students'),
    path('add_student/', views.add_student, name='add_student'),
    # Note: These URLs now take a student_id as an argument
    path('show_student_search/', views.show_student_search, name='show_student_search'),
    path('show_student/<int:student_id>/', views.show_student, name='show_student'),
    path('edit_student_search/', views.edit_student_search, name='edit_student_search'),
    path('edit_student/<int:student_id>/', views.edit_student, name='edit_student'),
    path('delete_student_search/', views.delete_student_search, name='delete_student_search'),
    path('delete_student/<int:student_id>/', views.delete_student, name='delete_student'),
    path('settings/', views.system_settings, name='settings'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
