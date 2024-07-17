from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from app.models import Course, Student, customuser, Staff

@login_required(login_url='/')
def HOME(request):
    student_count = Student.objects.all().count()

    context = {
        'student_count': student_count,
    }
    return render(request, 'staff/home.html', context)

@login_required(login_url='/')
def STUDENTVIEW(request):
    student = Student.objects.all()

    context = {
        'student': student,
    }
    return render(request, 'staff/staff_viewstudent.html', context)

@login_required(login_url='/')
def VIEW_STUDENTS_JUNIOR1(request):
    students = Student.objects.filter(course_id__name='JUNIOR 1')
    return render(request, 'staff/View_Students/view_students_junior1.html', {'students': students})

@login_required(login_url='/')
def VIEW_STUDENTS_JUNIOR2(request):
    students = Student.objects.filter(course_id__name='JUNIOR 2')
    return render(request, 'staff/View_Students/view_students_junior2.html', {'students': students})

@login_required(login_url='/')
def VIEW_STUDENTS_JUNIOR3(request):
    students = Student.objects.filter(course_id__name='JUNIOR 3')
    return render(request, 'staff/View_Students/view_students_junior3.html', {'students': students})

@login_required(login_url='/')
def VIEW_STUDENTS_MIDDLE1(request):
    students = Student.objects.filter(course_id__name='MIDDLE 1')
    return render(request, 'staff/View_Students/view_students_middle1.html', {'students': students})

@login_required(login_url='/')
def VIEW_STUDENTS_MIDDLE2(request):
    students = Student.objects.filter(course_id__name='MIDDLE 2')
    return render(request, 'staff/View_Students/view_students_middle2.html', {'students': students})

@login_required(login_url='/')
def VIEW_STUDENTS_MIDDLE3(request):
    students = Student.objects.filter(course_id__name='MIDDLE 3')
    return render(request, 'staff/View_Students/view_students_middle3.html', {'students': students})

@login_required(login_url='/')
def VIEW_STUDENTS_MIDDLE4(request):
    students = Student.objects.filter(course_id__name='MIDDLE 4')
    return render(request, 'staff/View_Students/view_students_middle4.html', {'students': students})

@login_required(login_url='/')
def VIEW_STUDENTS_MIDDLE5(request):
    students = Student.objects.filter(course_id__name='MIDDLE 5')
    return render(request, 'staff/View_Students/view_students_middle5.html', {'students': students})

@login_required(login_url='/')
def VIEW_STUDENTS_NIOS1(request):
    students = Student.objects.filter(course_id__name='NIOS 1')
    return render(request, 'staff/View_Students/view_students_nios1.html', {'students': students})

@login_required(login_url='/')
def VIEW_STUDENTS_NIOS2(request):
    students = Student.objects.filter(course_id__name='NIOS 2')
    return render(request, 'staff/View_Students/view_students_nios2.html', {'students': students})

@login_required(login_url='/')
def VIEW_STUDENTS_NIOS3(request):
    students = Student.objects.filter(course_id__name='NIOS 3')
    return render(request, 'staff/View_Students/view_students_nios3.html', {'students': students})

@login_required(login_url='/')
def VIEW_STUDENTS_NIOS4(request):
    students = Student.objects.filter(course_id__name='NIOS 3')
    return render(request, 'staff/View_Students/view_students_nios4.html', {'students': students})

@login_required(login_url='/')
def VIEW_STUDENTS_NIOS5(request):
    students = Student.objects.filter(course_id__name='NIOS 3')
    return render(request, 'staff/View_Students/view_students_nios5.html', {'students': students})



