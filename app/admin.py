from django.contrib import admin
from .models import *
from .models import customuser, Course, Student

from django.contrib.auth.admin import UserAdmin

class UserModel(UserAdmin):
    list_display = ['username', 'user_type']

admin.site.register(customuser, UserModel)
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Staff)

