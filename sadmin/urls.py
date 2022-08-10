from django.urls import path
from . import views

urlpatterns=[
    path('login', views.scadmin_login),
    path('teacherslist', views.teachers_views),
    path('viewstudents', views.view_students)
]