from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
from .forms import StudentForm
from .models import Student

def home(request):
    """
    Renders the home page of the student management system.
    تعرض الصفحة الرئيسية لنظام إدارة الطلاب.
    """
    return render(request, 'student/home.html')

def all_students(request):
    """
    Displays a paginated list of all students.
    تعرض قائمة بجميع الطلاب مع ترقيم الصفحات.
    """
    student_list = Student.objects.all()
    paginator = Paginator(student_list, 10)  # Show 10 students per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'student/all_students.html', context)

def add_student(request):
    """
    Handles adding a new student.
    تتعامل مع إضافة طالب جديد.
    """
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'تم إضافة الطالب {form.cleaned_data["name"]} بنجاح')
            return redirect('all_students')
    else:
        form = StudentForm()
        
    context = {'form': form}
    return render(request, 'student/add_student.html', context)

def show_student_search(request):
    """
    Renders the search page for a student.
    تعرض صفحة البحث عن طالب.
    """
    student = None
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        try:
            student = Student.objects.get(pk=student_id)
            return redirect('show_student', student_id=student.id)
        except Student.DoesNotExist:
            messages.error(request, 'لم يتم العثور على الطالب')
            return redirect('show_student_search')
            
    return render(request, 'student/show_student.html', {'student': student})


def show_student(request, student_id):
    """
    Displays the details of a single student.
    تعرض تفاصيل طالب واحد.
    """
    student = get_object_or_404(Student, pk=student_id)
    context = {'student': student}
    return render(request, 'student/show_student.html', context)
    
    
def edit_student_search(request):
    """
    Renders the search page for editing a student.
    تعرض صفحة البحث لتعديل طالب.
    """
    student = None
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        try:
            student = Student.objects.get(pk=student_id)
            return redirect('edit_student', student_id=student.id)
        except Student.DoesNotExist:
            messages.error(request, 'لم يتم العثور على الطالب')
            return redirect('edit_student_search')
    
    return render(request, 'student/edit_student.html', {'student': student})


def edit_student(request, student_id):
    """
    Handles editing a student's data.
    تتعامل مع تعديل بيانات طالب.
    """
    student = get_object_or_404(Student, pk=student_id)
    
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, f'تم تحديث بيانات الطالب {student.name} بنجاح')
            return redirect('edit_student', student_id=student.id)
    else:
        form = StudentForm(instance=student)
    
    context = {'form': form, 'student': student}
    return render(request, 'student/edit_student.html', context)


def delete_student_search(request):
    """
    Renders the search page for deleting a student.
    تعرض صفحة البحث لحذف طالب.
    """
    student = None
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        try:
            student = Student.objects.get(pk=student_id)
            return redirect('delete_student', student_id=student.id)
        except Student.DoesNotExist:
            messages.error(request, 'لم يتم العثور على الطالب')
            return redirect('delete_student_search')
            
    return render(request, 'student/delete_student.html', {'student': student})


def delete_student(request, student_id):
    """
    Handles deleting a student.
    تتعامل مع حذف طالب.
    """
    student = get_object_or_404(Student, pk=student_id)
    
    if request.method == 'POST':
        student_name = student.name
        student.delete()
        messages.success(request, f'تم حذف الطالب {student_name} بنجاح')
        return redirect('all_students')
    
    context = {'student': student}
    return render(request, 'student/delete_student.html', context)


def system_settings(request):
    """
    Renders the settings page.
    تعرض صفحة الإعدادات.
    """
    return render(request, 'student/settings.html')
    
def dashboard(request):
    """
    Renders the dashboard page.
    تعرض صفحة لوحة التحكم.
    """
    return render(request, 'student/dashboard.html')

