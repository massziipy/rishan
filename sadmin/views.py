from django.shortcuts import render

# Create your views here.
def scadmin_login(request):
    return render(request,'home/login.html')

def teachers_views(request):
    return render(request,'home/teachersview.html')

def view_students(request):
    return render(request,'home/viewstudents.html')