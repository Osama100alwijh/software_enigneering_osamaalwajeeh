# students/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator

# قائمة الطلاب المعدلة لتصبح قائمة من القواميس
students = [
    {'id': 1, 'name': 'اسامه', 'age': 20, 'address': 'الرياض', 'phone': '1234567890', 'email': 'osama@example.com', 'college': 'الحاسبات', 'gpa': 3.8},
    {'id': 2, 'name': 'محمد', 'age': 22, 'address': 'جدة', 'phone': '0987654321', 'email': 'mahmed@example.com', 'college': 'الهندسة', 'gpa': 4.2},
    {'id': 3, 'name': 'علي', 'age': 21, 'address': 'الدمام', 'phone': '1122334455', 'email': 'ali@example.com', 'college': 'الطب', 'gpa': 4.7},
    {'id': 4, 'name': 'فاطمة', 'age': 23, 'address': 'المدينة', 'phone': '5566778899', 'email': 'fatima@example.com', 'college': 'الصيدلة', 'gpa': 3.9},
    {'id': 5, 'name': 'سارة', 'age': 19, 'address': 'الرياض', 'phone': '6677889900', 'email': 'sara@example.com', 'college': 'الآداب', 'gpa': 3.5},
    {'id': 6, 'name': 'يوسف', 'age': 20, 'address': 'جدة', 'phone': '7788990011', 'email': 'yousef@example.com', 'college': 'الحاسبات', 'gpa': 4.5},
    {'id': 7, 'name': 'ليلى', 'age': 21, 'address': 'الرياض', 'phone': '8899001122', 'email': 'layla@example.com', 'college': 'الهندسة', 'gpa': 4.1},
    {'id': 8, 'name': 'أحمد', 'age': 24, 'address': 'الدمام', 'phone': '9900112233', 'email': 'ahmed@example.com', 'college': 'الطب', 'gpa': 4.9},
    {'id': 9, 'name': 'نورة', 'age': 20, 'address': 'المدينة', 'phone': '0011223344', 'email': 'noura@example.com', 'college': 'الصيدلة', 'gpa': 3.7},
    {'id': 10, 'name': 'خالد', 'age': 22, 'address': 'الرياض', 'phone': '1122334455', 'email': 'khalid@example.com', 'college': 'الآداب', 'gpa': 3.2},
    {'id': 11, 'name': 'سعود', 'age': 21, 'address': 'جدة', 'phone': '2233445566', 'email': 'saud@example.com', 'college': 'الحاسبات', 'gpa': 4.0},
    {'id': 12, 'name': 'مريم', 'age': 23, 'address': 'الدمام', 'phone': '3344556677', 'email': 'maryam@example.com', 'college': 'الهندسة', 'gpa': 4.6},
]
# هذه الفئة تحاكي نموذج Django
class Student:
    def __init__(self, id, name, age, address, phone, email, college, gpa):
        self.id = id
        self.name = name
        self.age = age
        self.address = address
        self.phone = phone
        self.email = email
        self.college = college
        self.gpa = gpa
        
# هذه الوظيفة تحاكي نموذج Form للتحقق من الصحة
class StudentForm:
    def __init__(self, data=None, initial=None):
        self.data = data
        self.initial = initial
        self.errors = {}
        self.cleaned_data = {}

    def is_valid(self):
        # هنا يمكنك إضافة منطق التحقق من صحة البيانات
        # للتبسيط، سنفترض أن البيانات دائماً صحيحة
        self.cleaned_data = self.data
        return True

# الحصول على أقصى رقم ID
def get_next_id():
    return max([s['id'] for s in students]) + 1 if students else 1

# الصفحات الرئيسية
def home(request):
    return render(request, 'students/home.html')

def all_students(request):
    student_list = students
    paginator = Paginator(student_list, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'students/all_students.html', {'page_obj': page_obj})

def add_student(request):
    if request.method == 'POST':
        form_data = dict(request.POST.items())
        form = StudentForm(data=form_data)
        if form.is_valid():
            new_student = form.cleaned_data
            new_student['id'] = get_next_id()
            new_student['gpa'] = float(new_student['gpa'])
            new_student['age'] = int(new_student['age'])
            students.append(new_student)
            messages.success(request, 'تم إضافة الطالب بنجاح.')
            return redirect('all_students')
    else:
        form = StudentForm()
    return render(request, 'students/add_student.html', {'form': form})

# البحث عن طالب
def show_student_search(request):
    student = None
    if request.method == 'POST':
        student_id_str = request.POST.get('student_id')
        try:
            student_id = int(student_id_str)
            student = next((s for s in students if s['id'] == student_id), None)
            if not student:
                messages.error(request, 'لم يتم العثور على الطالب.')
        except (ValueError, TypeError):
            messages.error(request, 'الرقم الجامعي غير صالح.')
    return render(request, 'students/show_student.html', {'student': student})

# عرض بيانات طالب
def show_student_data(request, student_id):
    student = next((s for s in students if s['id'] == student_id), None)
    if not student:
        messages.error(request, 'لم يتم العثور على الطالب.')
        return redirect('show_student_search')
    return render(request, 'students/show_student.html', {'student': student})

# تعديل طالب
def edit_student_search(request):
    student = None
    if request.method == 'POST':
        student_id_str = request.POST.get('student_id')
        try:
            student_id = int(student_id_str)
            student = next((s for s in students if s['id'] == student_id), None)
            if student:
                return redirect('edit_student', student_id=student_id)
            else:
                messages.error(request, 'لم يتم العثور على الطالب.')
        except (ValueError, TypeError):
            messages.error(request, 'الرقم الجامعي غير صالح.')
    return render(request, 'students/edit_student.html', {'student': None})


def edit_student(request, student_id):
    student = next((s for s in students if s['id'] == student_id), None)
    
    if not student:
        messages.error(request, 'لم يتم العثور على الطالب.')
        return redirect('edit_student_search')

    if request.method == 'POST':
        form_data = dict(request.POST.items())
        form = StudentForm(data=form_data)
        if form.is_valid():
            edited_data = form.cleaned_data
            student.update({
                'name': edited_data['name'],
                'age': int(edited_data['age']),
                'address': edited_data['address'],
                'phone': edited_data['phone'],
                'email': edited_data['email'],
                'college': edited_data['college'],
                'gpa': float(edited_data['gpa'])
            })
            messages.success(request, 'تم تحديث بيانات الطالب بنجاح.')
            return redirect('all_students')
    else:
        form = StudentForm(initial=student)
    
    context = {'form': form, 'student': student}
    return render(request, 'students/edit_student.html', context)
    
# حذف طالب
def delete_student_search(request):
    student = None
    if request.method == 'POST':
        student_id_str = request.POST.get('student_id')
        try:
            student_id = int(student_id_str)
            student = next((s for s in students if s['id'] == student_id), None)
            if not student:
                messages.error(request, 'لم يتم العثور على الطالب.')
        except (ValueError, TypeError):
            messages.error(request, 'الرقم الجامعي غير صالح.')

    return render(request, 'students/delete_student.html', {'student': student})


def delete_student(request, student_id):
    global students
    student = next((s for s in students if s['id'] == student_id), None)
    
    if student:
        if request.method == 'POST':
            students = [s for s in students if s['id'] != student['id']]
            messages.success(request, f'تم حذف الطالب {student["name"]} بنجاح')
            return redirect('all_students')
        else:
            context = {'student': student}
            return render(request, 'students/delete_student.html', context)
    else:
        messages.error(request, 'لم يتم العثور على الطالب.')
        return redirect('delete_student_search')


# لوحة التحكم
def dashboard(request):
    total_students = len(students)
    if total_students > 0:
        total_gpa = sum(s['gpa'] for s in students)
        average_gpa = total_gpa / total_students
        highest_gpa = max(s['gpa'] for s in students)

        colleges = {}
        for s in students:
            colleges[s['college']] = colleges.get(s['college'], 0) + 1
        
        gpa_data = {'labels': [], 'values': []}
        for s in students:
            gpa_range = ''
            if s['gpa'] >= 4.5: gpa_range = '4.5 - 5.0'
            elif s['gpa'] >= 4.0: gpa_range = '4.0 - 4.49'
            elif s['gpa'] >= 3.0: gpa_range = '3.0 - 3.99'
            else: gpa_range = '< 3.0'
            
            if gpa_range not in gpa_data['labels']:
                gpa_data['labels'].append(gpa_range)
                gpa_data['values'].append(1)
            else:
                index = gpa_data['labels'].index(gpa_range)
                gpa_data['values'][index] += 1
                
        context = {
            'total_students': total_students,
            'average_gpa': f'{average_gpa:.2f}',
            'highest_gpa': highest_gpa,
            'college_labels': list(colleges.keys()),
            'college_counts': list(colleges.values()),
            'gpa_labels': gpa_data['labels'],
            'gpa_values': gpa_data['values']
        }
    else:
        context = {
            'total_students': 0,
            'average_gpa': '0.00',
            'highest_gpa': '0.00',
            'college_labels': [],
            'college_counts': [],
            'gpa_labels': [],
            'gpa_values': []
        }
    return render(request, 'students/dashboard.html', context)

# الإعدادات
def settings(request):
    return render(request, 'students/settings.html')
