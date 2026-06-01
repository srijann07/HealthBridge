from django.shortcuts import render

def doctor_login(request):
    return render(request, 'core/doctor_login.html')

def doctor_register(request):
    return render(request, 'core/doctor_register.html')

def doctor_dashboard(request):
    return render(request, 'core/doctor_dashboard.html')