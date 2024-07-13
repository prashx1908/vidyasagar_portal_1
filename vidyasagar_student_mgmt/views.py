from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from app.emailbackend import EmailBackEnd
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
from app.models import customuser, Course
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model

def create_super_user(username, email, password):
    User = get_user_model()
    if not User.objects.filter(username=username).exists():
        user = User.objects.create_superuser(username, email, password)
        user.user_type = '1'  # Set user_type as admin
        user.save()
    else:
        user = User.objects.get(username=username)
        if not user.is_superuser:
            user.is_superuser = True
            user.user_type = '1'  # Set user_type as admin
            user.save()
        else:
            print(f"Superuser '{username}' already exists.")

def BASE(request):
    return render(request,'base.html')


def doLogin(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Authenticate user
        user = authenticate(request, username=email, password=password)

        if user is not None:
            # Log in the user
            login(request, user)

            # Check user_type and redirect accordingly
            if user.user_type == '1':  # Admin
                return redirect('hod_home')
            elif user.user_type == '2':  # Staff
                return redirect('staff_home')
            elif user.user_type == '3':  # Student
                return redirect('student_home')
            else:
                # Handle unexpected user_type (though it should be one of '1', '2', '3')
                messages.error(request, "Invalid user type")
                return redirect('login')
        else:
            # Handle invalid login credentials
            messages.error(request, "Invalid credentials")
            return redirect('login')

    # If not a POST request, redirect to login page
    return redirect('login')

def doLogout(request):
    logout(request)
    return redirect('login')


def PROFILE(request):
    user= customuser.objects.get(id= request.user.id)

    context = {
        "user": user,
    }

    return render(request, 'profile.html')


def PROFILE_UPDATE(request):
    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')

        try:
            user = customuser.objects.get(id=request.user.id)
            user.first_name = first_name
            user.last_name = last_name

            if password !=None and password != "" :
                user.set_password(password)

            user.save()
            messages.success(request, 'Your Profile Updated Successfully !!')
            return redirect('profile')
        except customuser.DoesNotExist:
            messages.error(request, 'User does not exist!')
        except Exception as e:
            messages.error(request, f'Failed to update profile! Error: {e}')

    return render(request, 'profile.html')


    return render(request, 'profile.html')

# views.py




def LOGIN(request):
    return render(request, 'login.html')