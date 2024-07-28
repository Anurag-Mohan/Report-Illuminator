from django.shortcuts import render, redirect , get_object_or_404
from .forms import BloodTestForm, ECGForm, LFTForm, KFTForm
from .conversion import (
    convert_blood_test_data, 
    convert_ecg_data,
    convert_lft_data, 
    convert_kft_data,
)
from .graphgenerations import (
    generate_blood_test_graph, 
    generate_ecg_graph,
    generate_lft_graph,
    generate_kft_graph
)
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import ConversionHistory
from django.utils.html import strip_tags
from .forms import SignUpForm
from .models import UserProfile

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def clear_history(request):
    user = request.user
    ConversionHistory.objects.filter(user=user).delete()
    messages.success(request, 'Your conversion history has been cleared successfully.')
    return redirect('dashboard')
    
@login_required
def delete_account(request):
    if request.method == 'POST':
        user = request.user
        user.delete()
        messages.success(request, 'Your account has been deleted successfully.')
        return redirect('home')
    return redirect('home')


def sign_up_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db() 
            user.userprofile.first_name = form.cleaned_data.get('first_name')
            user.userprofile.last_name = form.cleaned_data.get('last_name')
            user.userprofile.age = form.cleaned_data.get('age')
            user.userprofile.dob = form.cleaned_data.get('dob')
            user.userprofile.save()
            return redirect('login') 
    else:
        form = SignUpForm()
    return render(request, 'reports/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            return render(request, 'reports/login.html', {'error': 'Invalid username or password'})
    return render(request, 'reports/login.html')

def logout_view(request):
    auth_logout(request)
    return redirect('home')

def dashboard(request):
    user = request.user
    
    history = ConversionHistory.objects.filter(user=user).order_by('-date')
    for record in history:
        record.result = strip_tags(record.result)
    
    return render(request, 'reports/dashboard.html', {'history': history})

def conversion_detail(request, pk):
    entry = get_object_or_404(ConversionHistory, pk=pk)
    return render(request, 'reports/conversion_detail.html', {'entry': entry})
   

def home(request):
    return render(request, 'reports/home.html')

def convert_blood_test(request):
    if request.method == 'POST':
        form = BloodTestForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            result_data, current_values = convert_blood_test_data(form_data)
            graph_path = generate_blood_test_graph(result_data, current_values)
            readable_result = '<br>'.join([f'{label}: <span class="{cls}">{result}</span>' for label, result, cls in result_data])
            table_result = [(label, result, cls) for label, result, cls in result_data]
            
            if request.user.is_authenticated:
                ConversionHistory.objects.create(
                    user=request.user,
                    conversion_type='Blood Test',
                    result=readable_result
                )
            
            return render(request, 'reports/result.html', {'result': readable_result, 'table_result': table_result, 'graph_path': graph_path})
    else:
        form = BloodTestForm()
    return render(request, 'reports/blood_test.html', {'form': form})

def convert_ecg(request):
    if request.method == 'POST':
        form = ECGForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            result_data, current_values = convert_ecg_data(form_data)
            graph_path = generate_ecg_graph(result_data, current_values)
            readable_result = '<br>'.join([f'{label}: <span class="{cls}">{result}</span>' for label, result, cls in result_data])
            table_result = [(label, result, cls) for label, result, cls in result_data]
            
            if request.user.is_authenticated:
                ConversionHistory.objects.create(
                    user=request.user,
                    conversion_type='ECG',
                    result=readable_result
                )
            
            return render(request, 'reports/result.html', {'result': readable_result, 'table_result': table_result, 'graph_path': graph_path})
    else:
        form = ECGForm()
    return render(request, 'reports/ecg.html', {'form': form})

def convert_lft(request):
    if request.method == 'POST':
        form = LFTForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            result_data, current_values = convert_lft_data(form_data)
            graph_path = generate_lft_graph(result_data, current_values)
            readable_result = '<br>'.join([f'{label}: <span class="{cls}">{result}</span>' for label, result, cls in result_data])
            table_result = [(label, result, cls) for label, result, cls in result_data]
            
            if request.user.is_authenticated:
                ConversionHistory.objects.create(
                    user=request.user,
                    conversion_type='LFT',
                    result=readable_result
                )
            
            return render(request, 'reports/result.html', {'result': readable_result, 'table_result': table_result, 'graph_path': graph_path})
    else:
        form = LFTForm()
    return render(request, 'reports/lft.html', {'form': form})

def convert_kift(request):
    if request.method == 'POST':
        form = KFTForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            result_data, current_values = convert_kft_data(form_data)
            graph_path = generate_kft_graph(result_data, current_values)
            readable_result = '<br>'.join([f'{label}: <span class="{cls}">{result}</span>' for label, result, cls in result_data])
            table_result = [(label, result, cls) for label, result, cls in result_data]
            
            if request.user.is_authenticated:
                ConversionHistory.objects.create(
                    user=request.user,
                    conversion_type='KFT',
                    result=readable_result
                )
            
            return render(request, 'reports/result.html', {'result': readable_result, 'table_result': table_result, 'graph_path': graph_path})
    else:
        form = KFTForm()
    return render(request, 'reports/kft.html', {'form': form})
