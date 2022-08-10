from django.urls import path
from . import views

urlpatterns=[
    path('login', views.teacher_login),
    path('attendance', views.attendance),
    path('students', views.students),
    path('addmarks', views.add_marks)
]