from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from app.models import Course, Student, customuser, Staff
from django.shortcuts import get_object_or_404
from app.emailbackend import EmailBackEnd

@login_required(login_url='/')
def HOME(request):
    student_count= Student.objects.all().count()

    student_gender_male= Student.objects.filter(gender='Male').count()
    student_gender_female = Student.objects.filter(gender='Female').count()

    context = {
        'student_count':student_count,
        'student_gender_male':student_gender_male,
        'student_gender_female':student_gender_female

    }
    return render(request, 'Hod/home.html',context)
@login_required(login_url='/')
def ADD_STUDENT(request):
    courses = Course.objects.all()

    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        course_id = request.POST.get('course_id')
        student_details_link = request.POST.get('student_details_link')

        # Ensure course_id is valid
        if course_id == "Select Course" or not course_id.isdigit():
            messages.error(request, "Please select a valid course.")
            return redirect('add_student')  # Replace with your actual add student URL name

        course_id = int(course_id)

        if customuser.objects.filter(email=email).exists():
            messages.warning(request, 'Email is already taken')
            return redirect('add_student')

        if customuser.objects.filter(username=username).exists():
            messages.warning(request, 'Username is already taken')
            return redirect('add_student')

        # Create CustomUser (Student) object
        if password == password2:
            user = customuser(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                profile_pic=profile_pic,
                user_type=3,
                student_details_link=student_details_link,
            )
            user.set_password(password)
            user.save()

            course = Course.objects.get(id=course_id)

            # Create Student object
            student = Student(
                admin=user,
                address=address,
                gender=gender,
                course_id=course,
            )
            student.save()

            messages.success(request, user.first_name + " " + user.last_name + " successfully added")
            return redirect('add_student')
        else:
            messages.error(request, "Passwords do not match")
            return redirect('add_student')

    context = {
        'courses': courses,
    }
    return render(request, 'Hod/add_student.html', context)


def VIEW_STUDENT(request):
    student = Student.objects.all()


    context={
        'student': student,
    }
    return render(request, 'Hod/view_student.html',context)


def EDIT_STUDENT(request, id):
    student = Student.objects.filter(id= id)
    course= Course.objects.all()

    context = {
        'student': student,
        'course': course,
    }

    return render(request,'Hod/edit_student.html',context)


def UPDATE_STUDENT(request):
    if request.method=='POST':
        student_id = request.POST.get('student_id')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        address = request.POST.get('address')
        gender = request.POST.get('gender')
        course_id = request.POST.get('course_id')
        student_details_link = request.POST.get('student_details_link')

        if course_id == "Select Course":
            messages.error(request, "Please select a valid course.")
            return redirect('edit_student', id=student_id)

        user= customuser.objects.get(id = student_id)
        user.first_name= first_name
        user.last_name=last_name
        user.email=email
        user.username=username
        user.student_details_link = student_details_link

        if password and password2:
            if password == password2:
                user.set_password(password)
            else:
                messages.error(request, "Passwords do not match")
                return redirect('edit_student', id=student_id)

        if password != None and password != "":
            user.set_password(password)
        user.save()

        student= get_object_or_404(Student, admin=user)
        student.address=address
        student.gender=gender

        course= get_object_or_404(Course, id=int(course_id))
        student.course_id= course

        student.save()
        messages.success(request,'Records Updated')
        return redirect('view_student')



    return render(request,'Hod/edit_student.html')


def DELETE_STUDENT(request, admin):
    student = get_object_or_404(customuser, id=admin)
    student.delete()
    messages.success(request, 'Student successfully deleted')
    return redirect('view_student')


def ADD_STAFF(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        department = request.POST.get('department')
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        address = request.POST.get('address')
        gender = request.POST.get('gender')

        if customuser.objects.filter(email=email).exists():
            messages.warning(request, 'Email Is Already Taken')
            return redirect('add_staff')

        if customuser.objects.filter(username=username).exists():
            messages.warning(request, 'Username Is Already Taken')
            return redirect('add_staff')

            # Create CustomUser (Student) object
        if password == password2:
            user = customuser(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                department=department,
                user_type=2,

            )
            user.set_password(password)  # Correct method to set password
            user.save()

            staff =Staff(
                admin= user,
                address=address,
                gender=gender,
                department=department,


            )
            staff.save()
            messages.success(request, 'Staff Added')
            return redirect("add_staff")
        else:
            messages.warning(request, 'Password Does Not Match')


    return render(request, 'Hod/add_staff.html')


def VIEW_STAFF(request):
    staff = Staff.objects.all()

    context={
        'staff':staff,
}
    return render(request,'Hod/view_staff.html',context)


def EDIT_STAFF(request, id):
    staff = Staff.objects.get(id=id)

    context = {
        'staff': staff,
    }
    return render(request,'Hod/edit_staff.html',context)

def DELETE_STAFF(request, admin):
    staff = customuser.objects.get(id = admin)
    staff.delete()
    messages.success(request, 'Staff successfully deleted')
    return redirect('view_staff')


def UPDATE_STAFF(request):
    if request.method == 'POST':
        staff_id = request.POST.get('staff_id')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        department = request.POST.get('department')
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        address = request.POST.get('address')
        gender = request.POST.get('gender')

        # Retrieve the existing user and staff objects
        user = customuser.objects.get(id=staff_id)
        staff = get_object_or_404(Staff, admin=user)

        # Update user (customuser) details
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username
        user.department = department  # Ensure department is updated correctly

        if password:
            if password == password2:
                user.set_password(password)
            else:
                messages.error(request, "Passwords do not match")
                return redirect('edit_staff', id=staff_id)

        user.save()

        # Update staff details
        staff.address = address
        staff.gender = gender
        staff.department = department  # Ensure department is updated correctly

        staff.save()

        messages.success(request, 'Staff records updated successfully')
        return redirect('view_staff')

    return render(request, 'Hod/edit_staff.html')


def admin_view_timetable():
    return None
def admin_edit_timetable():
    return None
