# teacher_app/views.py
# This file handles the logic for the teacher management system.
# يتولى هذا الملف منطق نظام إدارة المعلمين.

from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from .forms import TeacherForm
from .models import Teacher

def home(request):
    """
    Renders the home page of the teacher management system.
    تعرض الصفحة الرئيسية لنظام إدارة المعلمين.
    """
    return render(request, 'teacher/home.html')

def all_teachers(request):
    """
    Displays a paginated list of all teachers.
    تعرض قائمة بجميع المعلمين مع ترقيم الصفحات.
    """
    teacher_list = list(Teacher.objects.all().values())
    paginator = Paginator(teacher_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'teacher/all_teachers.html', context)

def add_teacher(request):
    """
    Handles adding a new teacher.
    تتعامل مع إضافة معلم جديد.
    """
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'تم إضافة المعلم {form.cleaned_data["name"]} بنجاح')
            return redirect('add_teacher')
    else:
        form = TeacherForm()
    
    context = {'form': form}
    return render(request, 'teacher/add_teacher.html', context)

def show_teacher_search(request):
    """
    Renders the search page for displaying a teacher.
    تعرض صفحة البحث لعرض بيانات معلم.
    """
    return render(request, 'teacher/show_teacher.html')

def show_teacher(request, teacher_id):
    """
    Displays the details of a specific teacher.
    تعرض تفاصيل معلم معين.
    """
    try:
        teacher = Teacher.objects.get(pk=teacher_id)
        context = {'teacher': teacher}
        return render(request, 'teacher/show_teacher.html', context)
    except Teacher.DoesNotExist:
        messages.error(request, 'لم يتم العثور على المعلم')
        return redirect('show_teacher_search')

def edit_teacher_search(request):
    """
    Renders the search page for editing a teacher.
    تعرض صفحة البحث لتعديل بيانات معلم.
    """
    return render(request, 'teacher/edit_teacher.html')

def edit_teacher(request, teacher_id):
    """
    Handles editing an existing teacher's data.
    تتعامل مع تعديل بيانات معلم موجود.
    """
    try:
        teacher = Teacher.objects.get(pk=teacher_id)
    except Teacher.DoesNotExist:
        messages.error(request, 'لم يتم العثور على المعلم')
        return redirect('edit_teacher_search')

    if request.method == 'POST':
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            messages.success(request, f'تم تحديث بيانات المعلم {teacher.name} بنجاح')
            return redirect('edit_teacher', teacher_id=teacher.id)
    else:
        form = TeacherForm(instance=teacher)
    
    context = {'form': form, 'teacher': teacher}
    return render(request, 'teacher/edit_teacher.html', context)

def delete_teacher_search(request):
    """
    Renders the search page for deleting a teacher.
    تعرض صفحة البحث لحذف معلم.
    """
    return render(request, 'teacher/delete_teacher.html')

def delete_teacher(request, teacher_id):
    """
    Handles deleting a teacher.
    تتعامل مع حذف معلم.
    """
    try:
        teacher = Teacher.objects.get(pk=teacher_id)
    except Teacher.DoesNotExist:
        messages.error(request, 'لم يتم العثور على المعلم')
        return redirect('delete_teacher_search')

    if request.method == 'POST':
        teacher_name = teacher.name
        teacher.delete()
        messages.success(request, f'تم حذف المعلم {teacher_name} بنجاح')
        return redirect('all_teachers')
    
    context = {'teacher': teacher}
    return render(request, 'teacher/delete_teacher.html', context)

def system_settings(request):
    """
    Renders the settings page.
    تعرض صفحة الإعدادات.
    """
    return render(request, 'teacher/settings.html')

def dashboard(request):
    """
    Renders the dashboard page.
    تعرض صفحة لوحة التحكم.
    """
    return render(request, 'teacher/dashboard.html')

