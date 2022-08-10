from django.shortcuts import render

# Create your views here.
def teacher_login(request):
    return render(request,'teacherhome/teacherlogin.html')

def attendance(request):
    return render(request,'teacherhome/attendance.html')


def students(request):
    return render(request,'teacherhome/students.html')


def add_marks(request):
    return render(request,'teacherhome/addmarks.html')            