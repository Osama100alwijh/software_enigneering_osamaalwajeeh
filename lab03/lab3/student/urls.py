from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('student/', views.show_student, name='show_student'),
    path('edit_student/', views.edit_student, name='edit_student'),
    path('delete_student/', views.delete_student, name='delete_student'),
]