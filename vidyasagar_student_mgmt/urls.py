
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

from . import views, admin_views, staff_views, student_views



urlpatterns = [
    path("admin/", admin.site.urls),

    path("base/", views.BASE, name='base'),

    path("", views.LOGIN, name='login'),

    path("dologin", views.doLogin, name= "doLogin"),

    path("HOD/home/", admin_views.HOME, name='hod_home'),

    path("Hod/Student/Add", admin_views.ADD_STUDENT, name= 'add_student'),

    path("Hod/Student/View", admin_views.VIEW_STUDENT, name= 'view_student'),

    path("Hod/Student/Edit/<str:id>", admin_views.EDIT_STUDENT, name= 'edit_student'),

    path("Hod/Student/Update/", admin_views.UPDATE_STUDENT, name='update_student'),

    path("Hod/Student/Delete/<str:admin>", admin_views.DELETE_STUDENT, name='delete_student'),

    path("Hod/Staff/Add", admin_views.ADD_STAFF, name= 'add_staff'),
    path("Hod/Staff/View", admin_views.VIEW_STAFF, name= 'view_staff'),
    path("Hod/Staff/Edit/<str:id>", admin_views.EDIT_STAFF, name= 'edit_staff'),
    path("Hod/Staff/Delete/<str:admin>", admin_views.DELETE_STAFF, name= 'delete_staff'),
    path("Hod/Staff/Update/", admin_views.UPDATE_STAFF, name= 'update_staff'),
    path('Hod/timetable/<int:student_id>/', admin_views.admin_view_timetable, name='admin_view_timetable'),
    path('Hod/timetable/<int:student_id>/edit/', admin_views.admin_edit_timetable, name='admin_edit_timetable'),

    path("Profile", views.PROFILE, name= "profile"),

    path("Profile/update", views.PROFILE_UPDATE, name="profile_update"),

    path("dologout", views.doLogout, name= "logout"),

    path("Staff/Home", staff_views.HOME, name='staff_home'),
    path("Staff/View/Student", staff_views.STUDENTVIEW, name='staff_viewstudent'),
    path('staff/timetable/', staff_views.staff_view_all_timetables, name='staff_view_all_timetables'),

    path("Student/Home", student_views.HOME, name="student_home"),

    path('student/profile', student_views.student_profile, name='student_profile'),
    path('student/timetable/', student_views.student_view_own_timetable, name='student_view_own_timetable'),


] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
