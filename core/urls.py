from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),

    path('doctor-login/', views.doctor_login),
    path('doctor-register/', views.doctor_register),
    path('doctor-dashboard/', views.doctor_dashboard),

    path('patient-login/', views.patient_login),
    path('patient-register/', views.patient_register),
    path('patient-dashboard/', views.patient_dashboard),
]