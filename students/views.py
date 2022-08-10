from django.shortcuts import render

# Create your views here.
def students_login(request):
    return render(request,'sthome/studentlogin.html')

def view_marks(request):
    return render(request,'sthome/viewmarks.html')    

def view_profile(request):
    return render(request,'sthome/viewprofile.html')    

def fix(request):
    return render(request,'sthome/fix.html')    