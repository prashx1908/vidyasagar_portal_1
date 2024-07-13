from django.db import models
from django.contrib.auth.models import AbstractUser


class customuser(AbstractUser):
    USER_TYPES = (
        ('1', 'ADMIN'),
        ('2', 'STAFF'),
        ('3', 'STUDENT'),
    )
    user_type = models.CharField(choices=USER_TYPES, max_length=50, default='3')
    profile_pic = models.ImageField(upload_to='media/profile_pic', blank=True, null=True)
    student_details_link = models.URLField(max_length=200, null=True, blank=True)
    department = models.CharField(max_length=100, blank=True, null=True)


class Course(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Student(models.Model):
    admin = models. OneToOneField(customuser,on_delete=models.CASCADE)
    address = models.TextField()
    gender = models.CharField(max_length=100)
    course_id = models.ForeignKey(Course,on_delete = models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.admin.first_name + self.admin.last_name

class Staff(models.Model):
    admin = models.OneToOneField(customuser,on_delete=models.CASCADE)
    address = models.TextField()
    gender = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.admin.username







