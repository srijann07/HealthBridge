from django.shortcuts import render

def home(request):
    return render(request,'core/home.html')

def doctor_login(request):
    return render(request,'core/doctor_login.html')

def doctor_register(request):
    return render(request,'core/doctor_register.html')

def patient_login(request):
    return render(request,'core/patient_login.html')

def patient_register(request):
    return render(request,'core/patient_register.html')