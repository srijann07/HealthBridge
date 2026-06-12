from django.shortcuts import render


# Home Page
def home(request):
    return render(request, "core/home.html")


# Doctor Module
def doctor_login(request):
    return render(request, "core/doctor_login.html")


def doctor_register(request):
    return render(request, "core/doctor_register.html")


def doctor_dashboard(request):
    return render(request, "core/doctor_dashboard.html")


# Patient Module
def patient_login(request):
    return render(request, "core/patient_login.html")


def patient_register(request):
    return render(request, "core/patient_register.html")


def patient_dashboard(request):
    return render(request, "core/patient_dashboard.html")