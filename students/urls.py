from django.urls import path
from . import views

urlpatterns=[
    path('login', views.students_login, name='slogin'),
    path('viewmarks', views.view_marks, name='svmarks'),
    path('viewprofile', views.view_profile),
    path('fix', views.fix)
]
