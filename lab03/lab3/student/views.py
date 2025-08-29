from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')
def show_student(request):
    return render(request, 'student.html')
def edit_student(request):
    return render(request, 'edit_student.html')
def delete_student(request):
    return render(request, 'delete_student.html')
def home(request):
    return render(request, 'home.html')