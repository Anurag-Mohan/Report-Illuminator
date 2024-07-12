from django.shortcuts import render
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
            return render(request, 'reports/result.html', {'result': readable_result, 'table_result': table_result, 'graph_path': graph_path})
    else:
        form = KFTForm()
    return render(request, 'reports/kft.html', {'form': form})

    
