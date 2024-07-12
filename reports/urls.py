from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('convert_blood_test/', views.convert_blood_test, name='convert_blood_test'),
    path('convert_ecg/', views.convert_ecg, name='convert_ecg'),
    path('convert_lft/', views.convert_lft, name='convert_lft'),
    path('convert_kift/', views.convert_kift, name='convert_kift'),
    
]
