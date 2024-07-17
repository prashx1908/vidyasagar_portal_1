from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from app.models import Course, Student, customuser, Staff
from django.shortcuts import get_object_or_404
from django.contrib.auth.hashers import make_password
from app.emailbackend import EmailBackEnd
import csv
from django.http import HttpResponse

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
    return render(request, 'HOD/home.html',context)
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


@login_required(login_url='/')
def VIEW_STUDENT(request):
    students = Student.objects.filter(is_deleted=False)
    context = {
        'students': students,
    }
    return render(request, 'Hod/view_student.html', context)

@login_required(login_url='/')
def EDIT_STUDENT(request, id):
    student = Student.objects.filter(id= id)
    course= Course.objects.all()

    context = {
        'student': student,
        'course': course,
    }

    return render(request,'Hod/edit_student.html',context)


@login_required(login_url='/')
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

@login_required(login_url='/')
def DELETE_STUDENT(request, admin):
    student = get_object_or_404(customuser, id=admin)
    student.delete()
    messages.success(request, 'Student successfully deleted')
    return redirect('view_student')


@login_required(login_url='/')
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


@login_required(login_url='/')
def VIEW_STAFF(request):
    staff = Staff.objects.all()

    context={
        'staff':staff,
}
    return render(request,'Hod/view_staff.html',context)


@login_required(login_url='/')
def EDIT_STAFF(request, id):
    staff = Staff.objects.get(id=id)

    context = {
        'staff': staff,
    }
    return render(request,'Hod/edit_staff.html',context)

@login_required(login_url='/')
def DELETE_STAFF(request, admin):
    staff = get_object_or_404(customuser, id=admin)
    staff.is_deleted = True  # Assuming you have an `is_deleted` field
    staff.save()
    messages.success(request, 'Staff successfully deleted')
    return redirect('view_staff_bin')  # Redirect to the staff bin view


@login_required(login_url='/')
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

@login_required(login_url='/')
def view_students_junior1(request):
    students = Student.objects.filter(course_id__name='JUNIOR 1')
    context = {
        'students': students,
    }
    return render(request, 'Hod/View_Students/view_students_junior1.html', context)

@login_required(login_url='/')
def view_students_junior2(request):
    students = Student.objects.filter(course_id__name='JUNIOR 2')
    context = {
        'students': students,
    }
    return render(request, 'Hod/View_Students/view_students_junior2.html', context)

@login_required(login_url='/')
def view_students_junior3(request):
    students = Student.objects.filter(course_id__name='JUNIOR 3')
    context = {
        'students': students,
    }
    return render(request, 'Hod/View_Students/view_students_junior3.html', context)

@login_required(login_url='/')
def view_students_middle1(request):
    students = Student.objects.filter(course_id__name='MIDDLE 1')
    context = {
        'students': students,
    }
    return render(request, 'Hod/View_Students/view_students_middle1.html', context)

@login_required(login_url='/')
def view_students_middle2(request):
    students = Student.objects.filter(course_id__name='MIDDLE 2')
    context = {
        'students': students,
    }
    return render(request, 'Hod/View_Students/view_students_middle2.html', context)

@login_required(login_url='/')
def view_students_middle3(request):
    students = Student.objects.filter(course_id__name='MIDDLE 3')
    context = {
        'students': students,
    }
    return render(request, 'Hod/View_Students/view_students_middle3.html', context)

@login_required(login_url='/')
def view_students_middle4(request):
    students = Student.objects.filter(course_id__name='MIDDLE 4')
    context = {
        'students': students,
    }
    return render(request, 'Hod/View_Students/view_students_middle4.html', context)

@login_required(login_url='/')
def view_students_middle5(request):
    students = Student.objects.filter(course_id__name='MIDDLE 5')
    context = {
        'students': students,
    }
    return render(request, 'Hod/View_Students/view_students_middle5.html', context)

@login_required(login_url='/')
def view_students_nios1(request):
    students = Student.objects.filter(course_id__name='NIOS 1')
    context = {
        'students': students,
    }
    return render(request, 'Hod/View_Students/view_students_nios1.html', context)

@login_required(login_url='/')
def view_students_nios2(request):
    students = Student.objects.filter(course_id__name='NIOS 2')
    context = {
        'students': students,
    }
    return render(request, 'Hod/View_Students/view_students_nios2.html', context)

@login_required(login_url='/')
def view_students_nios3(request):
    students = Student.objects.filter(course_id__name='NIOS 3')
    context = {
        'students': students,
    }
    return render(request, 'Hod/View_Students/view_students_nios3.html', context)

@login_required(login_url='/')
def view_students_nios4(request):
    students = Student.objects.filter(course_id__name='NIOS 4')
    context = {
        'students': students,
    }
    return render(request, 'Hod/View_Students/view_students_nios4.html', context)

@login_required(login_url='/')
def view_students_nios5(request):
    students = Student.objects.filter(course_id__name='NIOS 5')
    context = {
        'students': students,
    }
    return render(request, 'Hod/View_Students/view_students_nios5.html', context)

@login_required(login_url='/')
def DELETE_STUDENT(request, admin):
    student = get_object_or_404(customuser, id=admin)
    # Set is_deleted flag instead of deleting the record
    student.student.is_deleted = True  # Assuming the relation is correct
    student.student.save()
    messages.success(request, 'Student successfully moved to the bin.')
    return redirect('view_bin')  # Redirect to the bin view page

@login_required(login_url='/')
def view_bin(request):
    deleted_students = Student.objects.filter(is_deleted=True)
    context = {
        'deleted_students': deleted_students,
    }
    return render(request, 'Hod/view_bin.html', context)

@login_required(login_url='/')
def restore_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    student.is_deleted = False
    student.save()
    messages.success(request, 'Student successfully restored.')
    return redirect('view_bin')  # Redirect to the bin view page

@login_required(login_url='/')
def permanent_delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    student.delete()  # This will permanently delete the record from the database
    messages.success(request, 'Student permanently deleted.')
    return redirect('view_bin')  # Redirect to the bin view page

@login_required(login_url='/')
def view_staff_bin(request):
    deleted_staff = customuser.objects.filter(is_deleted=True)  # Assuming you have an `is_deleted` field
    context = {
        'deleted_staff': deleted_staff,
    }
    return render(request, 'Hod/view_staff_bin.html', context)
@login_required(login_url='/')
def restore_staff(request, staff_id):
    staff = get_object_or_404(customuser, id=staff_id)
    staff.is_deleted = False
    staff.save()
    messages.success(request, 'Staff successfully restored')
    return redirect('view_staff_bin')  # Redirect to the staff bin view
@login_required(login_url='/')
def permanent_delete_staff(request, staff_id):
    staff = get_object_or_404(customuser, id=staff_id)
    staff.delete()  # Permanently delete the staff record
    messages.success(request, 'Staff permanently deleted')
    return redirect('view_staff_bin')  # Redirect to the staff bin view


@login_required(login_url='/')
def download_students_junior1(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="students_junior1.csv"'

    writer = csv.writer(response)
    writer.writerow(['ID', 'First Name', 'Last Name', 'Class', 'Gender', 'Email', 'Student Report', 'Address', 'Created On', 'Updated On'])

    students = Student.objects.filter(course_id__name='Junior 1')
    for student in students:
        writer.writerow([
            student.id,
            student.admin.first_name,
            student.admin.last_name,
            student.course_id.name,
            student.gender,
            student.admin.email,
            student.admin.student_details_link,
            student.address,
            student.created_at,
            student.updated_at
        ])

    return response

@login_required(login_url='/')
def download_students_junior1(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="students_junior1.csv"'

    writer = csv.writer(response)
    writer.writerow(['ID', 'First Name', 'Last Name', 'Class', 'Gender', 'Email', 'Student Report', 'Address', 'Created On', 'Updated On'])

    students = Student.objects.filter(course_id__name='JUNIOR 1')
    for student in students:
        writer.writerow([
            student.id,
            student.admin.first_name,
            student.admin.last_name,
            student.course_id.name,
            student.gender,
            student.admin.email,
            student.admin.student_details_link,
            student.address,
            student.created_at,
            student.updated_at
        ])

    return response
@login_required(login_url='/')
def download_students_junior2(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="students_junior2.csv"'

    writer = csv.writer(response)
    writer.writerow(['ID', 'First Name', 'Last Name', 'Class', 'Gender', 'Email', 'Student Report', 'Address', 'Created On', 'Updated On'])

    students = Student.objects.filter(course_id__name='JUNIOR 2')
    for student in students:
        writer.writerow([
            student.id,
            student.admin.first_name,
            student.admin.last_name,
            student.course_id.name,
            student.gender,
            student.admin.email,
            student.admin.student_details_link,
            student.address,
            student.created_at,
            student.updated_at
        ])

    return response
@login_required(login_url='/')
def download_students_junior3(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="students_junior3.csv"'

    writer = csv.writer(response)
    writer.writerow(['ID', 'First Name', 'Last Name', 'Class', 'Gender', 'Email', 'Student Report', 'Address', 'Created On', 'Updated On'])

    students = Student.objects.filter(course_id__name='JUNIOR 3')
    for student in students:
        writer.writerow([
            student.id,
            student.admin.first_name,
            student.admin.last_name,
            student.course_id.name,
            student.gender,
            student.admin.email,
            student.admin.student_details_link,
            student.address,
            student.created_at,
            student.updated_at
        ])

    return response

@login_required(login_url='/')
def download_students_middle1(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="students_middle1.csv"'

    writer = csv.writer(response)
    writer.writerow(['ID', 'First Name', 'Last Name', 'Class', 'Gender', 'Email', 'Student Report', 'Address', 'Created On', 'Updated On'])

    students = Student.objects.filter(course_id__name='MIDDLE 1')
    for student in students:
        writer.writerow([
            student.id,
            student.admin.first_name,
            student.admin.last_name,
            student.course_id.name,
            student.gender,
            student.admin.email,
            student.admin.student_details_link,
            student.address,
            student.created_at,
            student.updated_at
        ])

    return response

@login_required(login_url='/')
def download_students_middle2(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="students_middle2.csv"'

    writer = csv.writer(response)
    writer.writerow(['ID', 'First Name', 'Last Name', 'Class', 'Gender', 'Email', 'Student Report', 'Address', 'Created On', 'Updated On'])

    students = Student.objects.filter(course_id__name='MIDDLE 2')
    for student in students:
        writer.writerow([
            student.id,
            student.admin.first_name,
            student.admin.last_name,
            student.course_id.name,
            student.gender,
            student.admin.email,
            student.admin.student_details_link,
            student.address,
            student.created_at,
            student.updated_at
        ])

    return response

@login_required(login_url='/')
def download_students_middle3(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="students_middle3.csv"'

    writer = csv.writer(response)
    writer.writerow(['ID', 'First Name', 'Last Name', 'Class', 'Gender', 'Email', 'Student Report', 'Address', 'Created On', 'Updated On'])

    students = Student.objects.filter(course_id__name='MIDDLE 3')
    for student in students:
        writer.writerow([
            student.id,
            student.admin.first_name,
            student.admin.last_name,
            student.course_id.name,
            student.gender,
            student.admin.email,
            student.admin.student_details_link,
            student.address,
            student.created_at,
            student.updated_at
        ])

    return response

@login_required(login_url='/')
def download_students_middle4(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="students_middle4.csv"'

    writer = csv.writer(response)
    writer.writerow(['ID', 'First Name', 'Last Name', 'Class', 'Gender', 'Email', 'Student Report', 'Address', 'Created On', 'Updated On'])

    students = Student.objects.filter(course_id__name='MIDDLE 4')
    for student in students:
        writer.writerow([
            student.id,
            student.admin.first_name,
            student.admin.last_name,
            student.course_id.name,
            student.gender,
            student.admin.email,
            student.admin.student_details_link,
            student.address,
            student.created_at,
            student.updated_at
        ])

    return response

@login_required(login_url='/')
def download_students_middle5(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="students_middle5.csv"'

    writer = csv.writer(response)
    writer.writerow(['ID', 'First Name', 'Last Name', 'Class', 'Gender', 'Email', 'Student Report', 'Address', 'Created On', 'Updated On'])

    students = Student.objects.filter(course_id__name='MIDDLE 5')
    for student in students:
        writer.writerow([
            student.id,
            student.admin.first_name,
            student.admin.last_name,
            student.course_id.name,
            student.gender,
            student.admin.email,
            student.admin.student_details_link,
            student.address,
            student.created_at,
            student.updated_at
        ])

    return response


@login_required(login_url='/')
def download_students_nios1(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="students_nios1.csv"'

    writer = csv.writer(response)
    writer.writerow(['ID', 'First Name', 'Last Name', 'Class', 'Gender', 'Email', 'Student Report', 'Address', 'Created On', 'Updated On'])

    students = Student.objects.filter(course_id__name='NIOS 1')
    for student in students:
        writer.writerow([
            student.id,
            student.admin.first_name,
            student.admin.last_name,
            student.course_id.name,
            student.gender,
            student.admin.email,
            student.admin.student_details_link,
            student.address,
            student.created_at,
            student.updated_at
        ])

    return response

@login_required(login_url='/')
def download_students_nios2(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="students_nios2.csv"'

    writer = csv.writer(response)
    writer.writerow(['ID', 'First Name', 'Last Name', 'Class', 'Gender', 'Email', 'Student Report', 'Address', 'Created On', 'Updated On'])

    students = Student.objects.filter(course_id__name='NIOS 2')
    for student in students:
        writer.writerow([
            student.id,
            student.admin.first_name,
            student.admin.last_name,
            student.course_id.name,
            student.gender,
            student.admin.email,
            student.admin.student_details_link,
            student.address,
            student.created_at,
            student.updated_at
        ])

    return response

@login_required(login_url='/')
def download_students_nios3(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="students_nios3.csv"'

    writer = csv.writer(response)
    writer.writerow(['ID', 'First Name', 'Last Name', 'Class', 'Gender', 'Email', 'Student Report', 'Address', 'Created On', 'Updated On'])

    students = Student.objects.filter(course_id__name='NIOS 3')
    for student in students:
        writer.writerow([
            student.id,
            student.admin.first_name,
            student.admin.last_name,
            student.course_id.name,
            student.gender,
            student.admin.email,
            student.admin.student_details_link,
            student.address,
            student.created_at,
            student.updated_at
        ])

    return response

@login_required(login_url='/')
def download_students_nios4(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="students_nios4.csv"'

    writer = csv.writer(response)
    writer.writerow(['ID', 'First Name', 'Last Name', 'Class', 'Gender', 'Email', 'Student Report', 'Address', 'Created On', 'Updated On'])

    students = Student.objects.filter(course_id__name='NIOS 4')
    for student in students:
        writer.writerow([
            student.id,
            student.admin.first_name,
            student.admin.last_name,
            student.course_id.name,
            student.gender,
            student.admin.email,
            student.admin.student_details_link,
            student.address,
            student.created_at,
            student.updated_at
        ])

    return response

@login_required(login_url='/')
def download_students_nios5(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="students_nios5.csv"'

    writer = csv.writer(response)
    writer.writerow(['ID', 'First Name', 'Last Name', 'Class', 'Gender', 'Email', 'Student Report', 'Address', 'Created On', 'Updated On'])

    students = Student.objects.filter(course_id__name='NIOS 5')
    for student in students:
        writer.writerow([
            student.id,
            student.admin.first_name,
            student.admin.last_name,
            student.course_id.name,
            student.gender,
            student.admin.email,
            student.admin.student_details_link,
            student.address,
            student.created_at,
            student.updated_at
        ])

    return response


def download_staff_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="staff_details.csv"'

    writer = csv.writer(response)
    writer.writerow(['First Name', 'Last Name', 'Email', 'Department', 'Username', 'Address', 'Gender'])

    staff_members = Staff.objects.all()
    for staff in staff_members:
        writer.writerow([staff.admin.first_name, staff.admin.last_name, staff.admin.email, staff.department, staff.admin.username, staff.address, staff.gender])

    return response