from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views
from . import admin_views, staff_views, student_views

from . import views, admin_views, staff_views, student_views

urlpatterns = [
    path("admin/", admin.site.urls),

    path("base/", views.BASE, name='base'),

    path("", views.LOGIN, name='login'),


    path("dologin", views.doLogin, name="doLogin"),


    path("dologin", views.doLogin, name="doLogin"),

    path("HOD/home/", admin_views.HOME, name='hod_home'),

    path("Hod/Student/Add", admin_views.ADD_STUDENT, name='add_student'),
    path("Hod/Student/View", admin_views.VIEW_STUDENT, name='view_student'),
    path("Hod/Student/Edit/<str:id>", admin_views.EDIT_STUDENT, name='edit_student'),
    path("Hod/Student/Update/", admin_views.UPDATE_STUDENT, name='update_student'),
    path("Hod/Student/Delete/<str:admin>", admin_views.DELETE_STUDENT, name='delete_student'),
                  path("Hod/Student/Delete/<int:student_id>", admin_views.DELETE_STUDENT, name='delete_student'),
                  path("Hod/Student/Bin", admin_views.view_bin, name='view_bin'),
                  path("Hod/Student/Restore/<int:student_id>", admin_views.restore_student, name='restore_student'),
                  path("Hod/Student/PermanentlyDelete/<int:student_id>", admin_views.permanent_delete_student,
                       name='permanent_delete_student'),

    path("Hod/Staff/Add", admin_views.ADD_STAFF, name='add_staff'),
    path("Hod/Staff/View", admin_views.VIEW_STAFF, name='view_staff'),
    path("Hod/Staff/Edit/<str:id>", admin_views.EDIT_STAFF, name='edit_staff'),
    path("Hod/Staff/Delete/<str:admin>", admin_views.DELETE_STAFF, name='delete_staff'),
    path("Hod/Staff/Update/", admin_views.UPDATE_STAFF, name='update_staff'),

# In your urls.py
path('Hod/Staff/Bin/', admin_views.view_staff_bin, name='view_staff_bin'),
path('Hod/Staff/Restore/<int:staff_id>/', admin_views.restore_staff, name='restore_staff'),
path('Hod/Staff/PermanentlyDelete/<int:staff_id>/', admin_views.permanent_delete_staff, name='permanent_delete_staff'),
    path("Profile", views.PROFILE, name="profile"),
    path("Profile/update", views.PROFILE_UPDATE, name="profile_update"),



    path('Hod/timetable/<int:student_id>/', admin_views.admin_view_timetable, name='admin_view_timetable'),
    path('Hod/timetable/<int:student_id>/edit/', admin_views.admin_edit_timetable, name='admin_edit_timetable'),

    path("Profile", views.PROFILE, name="profile"),
    path("Profile/update", views.PROFILE_UPDATE, name="profile_update"),

    path("dologout", views.doLogout, name="logout"),

    path("Staff/Home", staff_views.HOME, name='staff_home'),
    path("Staff/View/Student", staff_views.STUDENTVIEW, name='staff_viewstudent'),

    # Adding specific student views for staff
    path("Staff/View/Students/Junior1", staff_views.VIEW_STUDENTS_JUNIOR1, name='staff_view_students_junior1'),
    path("Staff/View/Students/Junior2", staff_views.VIEW_STUDENTS_JUNIOR2, name='staff_view_students_junior2'),
    path("Staff/View/Students/Junior3", staff_views.VIEW_STUDENTS_JUNIOR3, name='staff_view_students_junior3'),
    path("Staff/View/Students/Middle1", staff_views.VIEW_STUDENTS_MIDDLE1, name='staff_view_students_middle1'),
    path("Staff/View/Students/Middle2", staff_views.VIEW_STUDENTS_MIDDLE2, name='staff_view_students_middle2'),
    path("Staff/View/Students/Middle3", staff_views.VIEW_STUDENTS_MIDDLE3, name='staff_view_students_middle3'),
    path("Staff/View/Students/Middle4", staff_views.VIEW_STUDENTS_MIDDLE4, name='staff_view_students_middle4'),
    path("Staff/View/Students/Middle5", staff_views.VIEW_STUDENTS_MIDDLE5, name='staff_view_students_middle5'),
    path("Staff/View/Students/Nios1", staff_views.VIEW_STUDENTS_NIOS1, name='staff_view_students_nios1'),
    path("Staff/View/Students/Nios2", staff_views.VIEW_STUDENTS_NIOS2, name='staff_view_students_nios2'),
    path("Staff/View/Students/Nios3", staff_views.VIEW_STUDENTS_NIOS3, name='staff_view_students_nios3'),
    path("Staff/View/Students/Nios4", staff_views.VIEW_STUDENTS_NIOS4, name='staff_view_students_nios4'),
    path("Staff/View/Students/Nios5", staff_views.VIEW_STUDENTS_NIOS5, name='staff_view_students_nios5'),

                  path("Hod/Students/View/Junior1", admin_views.view_students_junior1,
                       name='hod_view_students_junior1'),
                  path("Hod/Students/View/Junior2", admin_views.view_students_junior2,
                       name='hod_view_students_junior2'),
                  path("Hod/Students/View/Junior3", admin_views.view_students_junior3,
                       name='hod_view_students_junior3'),

                  path("Hod/Students/View/Middle1", admin_views.view_students_middle1,
                       name='hod_view_students_middle1'),
                  path("Hod/Students/View/Middle2", admin_views.view_students_middle2,
                       name='hod_view_students_middle2'),
                  path("Hod/Students/View/Middle3", admin_views.view_students_middle3,
                       name='hod_view_students_middle3'),
                  path("Hod/Students/View/Middle4", admin_views.view_students_middle4,
                       name='hod_view_students_middle4'),
                  path("Hod/Students/View/Middle5", admin_views.view_students_middle5,
                       name='hod_view_students_middle5'),

                  path("Hod/Students/View/Nios1", admin_views.view_students_nios1, name='hod_view_students_nios1'),
                  path("Hod/Students/View/Nios2", admin_views.view_students_nios2, name='hod_view_students_nios2'),
                  path("Hod/Students/View/Nios3", admin_views.view_students_nios3, name='hod_view_students_nios3'),
                  path("Hod/Students/View/Nios4", admin_views.view_students_nios4, name='hod_view_students_nios4'),
                  path("Hod/Students/View/Nios5", admin_views.view_students_nios5, name='hod_view_students_nios5'),

    path('students/junior1/download/', admin_views.download_students_junior1, name='download_students_junior1'),
path('students/junior2/download/', admin_views.download_students_junior2, name='download_students_junior2'),
path('students/junior3/download/', admin_views.download_students_junior3, name='download_students_junior3'),
path('students/middle1/download/', admin_views.download_students_middle1, name='download_students_middle1'),
path('students/middle2/download/', admin_views.download_students_middle2, name='download_students_middle2'),
path('students/middle3/download/', admin_views.download_students_middle3, name='download_students_middle3'),
path('students/middle4/download/', admin_views.download_students_middle4, name='download_students_middle4'),
path('students/middle5/download/', admin_views.download_students_middle5, name='download_students_middle5'),
path('students/nios1/download/', admin_views.download_students_nios1, name='download_students_nios1'),
path('students/nios2/download/', admin_views.download_students_nios2, name='download_students_nios2'),
path('students/nios3/download/', admin_views.download_students_nios3, name='download_students_nios3'),
path('students/nios4/download/', admin_views.download_students_nios4, name='download_students_nios4'),
path('students/nios5/download/', admin_views.download_students_nios5, name='download_students_nios5'),
path('download_staff_csv/', admin_views.download_staff_csv, name='download_staff_csv'),



    path("Student/Home", student_views.HOME, name="student_home"),

    path("student/profile", student_views.student_profile, name='student_profile'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()

    path('student/profile', student_views.student_profile, name='student_profile'),
    path('student/timetable/', student_views.student_view_own_timetable, name='student_view_own_timetable'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()

