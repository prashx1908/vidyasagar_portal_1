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
    return render(request, 'Student/home.html',context)


@login_required(login_url='/')
def student_profile(request):
    user = customuser.objects.get(id=request.user.id)
    student = Student.objects.get(admin=user)

    context = {
        "user": user,
        "student": student,
    }
    return render(request, 'Student/profile.html', context)


def student_view_own_timetable():
    return None