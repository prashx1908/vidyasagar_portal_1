from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from app.models import Course, Student, customuser, Staff
from django.shortcuts import get_object_or_404

@login_required(login_url='/')
def HOME(request):
    student_count= Student.objects.all().count()

    context = {
        'student_count':student_count,
    }
    return render(request, 'staff/home.html',context)


def STUDENTVIEW(request):
    student = Student.objects.all()

    context = {
        'student': student,
    }
    return render(request, 'staff/staff_viewstudent.html', context)


def staff_view_all_timetables():
    return None