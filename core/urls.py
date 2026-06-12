from django.urls import path
from . import views

urlpatterns = [

    # Home
    path('', views.home, name='home'),

    # Doctor
    path('doctor-login/', views.doctor_login, name='doctor_login'),
    path('doctor-register/', views.doctor_register, name='doctor_register'),
    path('doctor-dashboard/', views.doctor_dashboard, name='doctor_dashboard'),

    # Patient
    path('patient-login/', views.patient_login, name='patient_login'),
    path('patient-register/', views.patient_register, name='patient_register'),
    path('patient-dashboard/', views.patient_dashboard, name='patient_dashboard'),

]