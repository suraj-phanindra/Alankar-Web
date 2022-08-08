from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'alankaar_home.html')


def volunteer(request):
    return render(request, 'volunteer_page.html')


def student(request):
    return render(request, 'student_registration.html')


def volunteer_registration(request):
    return render(request, 'volunteer_registration.html')


def student_reg_2(request):
    return render(request,'student_registraion_2.html')