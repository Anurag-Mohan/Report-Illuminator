from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.sign_up_view, name='sign_up_view'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('delete_account/', views.delete_account, name='delete_account'),
    path('clear_history/', views.clear_history, name='clear_history'),
    path('conversion/<int:pk>/', views.conversion_detail, name='conversion_detail'),
    path('', views.home, name='home'),
    path('convert_blood_test/', views.convert_blood_test, name='convert_blood_test'),
    path('convert_ecg/', views.convert_ecg, name='convert_ecg'),
    path('convert_lft/', views.convert_lft, name='convert_lft'),
    path('convert_kift/', views.convert_kift, name='convert_kift'),
    
]
