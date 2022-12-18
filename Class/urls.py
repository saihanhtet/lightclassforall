from django.urls import path
from . import views

urlpatterns = [
    path('',views.dashboard,name='Home'),
    path('save/',views.export_to_csv,name="export"),
    path("signup/", views.signup_user, name="Signup"),
    path("login/", views.login_user, name="Login"),
    path("logout/", views.logout_user, name="Logout"),
    path('course/',views.course,name='Course'),
    path('register/',views.register,name='Register'),
    path('completed/',views.completed,name='Completed'),
    path('inquery/',views.inquery,name='InQuery'),
    path('inquery_register/',views.inquery_register,name='InQueryRegister'),
    path('dropout/',views.dropout,name='Dropout'),
    path('student/',views.student,name="Student"),
    path('search/',views.search,name="Search"),
    path('studentinfo/<str:data>/',views.studentinfo,name='StudentInfo'),
    path('queryinfo/<str:data>/',views.queryinfo,name='QueryInfo'),
    path('updatequery/<str:data>/',views.querytostu,name='QueryToStu'),
    path('updatestudent/<str:data>/',views.updateStudent,name='UpdateStudent'),
    path('deletestudent/<str:data>/',views.deleteStudent,name='DeleteStudent'),
    path('courseinfo/<str:courseid>/',views.courseInfo,name='CourseInfo')
]