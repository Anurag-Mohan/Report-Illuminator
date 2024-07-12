import os
import numpy as np
import matplotlib.pyplot as plt
from django.conf import settings

def generate_blood_test_graph(result_data, current_values):
    labels = ['Hemoglobin', 'White Blood Cells', 'Platelets', 'RBC', 'Hematocrit', 'Glucose']
    normal_ranges = {
        'Hemoglobin': (13.5, 17.5),
        'White Blood Cells': (4.5, 11.0),
        'Platelets': (150, 450),
        'RBC': (4.7, 6.1),
        'Hematocrit': (40, 52),
        'Glucose': (70, 140)
    }

    x = np.arange(len(labels))
    width = 0.35
    colors = ['royalblue', 'green', 'red']
    fig, ax = plt.subplots(figsize=(10, 7), facecolor='violet')
    ax.bar(x - width/2, [normal_ranges[label][0] for label in labels], width, label='Normal Min', color=colors[0])
    ax.bar(x - width/2, [normal_ranges[label][1] for label in labels], width, bottom=[normal_ranges[label][0] for label in labels], label='Normal Max', color=colors[1])
    ax.bar(x + width/2, current_values, width, label='Current Value', color=colors[2])

    ax.set_xlabel('Parameters')
    ax.set_ylabel('Values')
    ax.set_title('Blood Test Parameters Comparison')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()
    ax.set_facecolor('yellow')
    plt.yscale('linear')
    fig.tight_layout()

    graph_path = os.path.join(settings.STATICFILES_DIRS[0], 'images', 'graph.png')
    plt.savefig(graph_path)
    plt.close()

    return graph_path

def generate_ecg_graph(result_data, current_values):
    labels = ['Heart Rate', 'PR Interval', 'QRS Duration', 'QT Interval']
    normal_ranges = {
        'Heart Rate': (60, 100),
        'PR Interval': (120, 200),
        'QRS Duration': (80, 120),
        'QT Interval': (340, 440)
    }

    x = np.arange(len(labels))
    width = 0.35
    colors = ['royalblue', 'green', 'red']
    fig, ax = plt.subplots(figsize=(10, 7), facecolor='yellow')
    ax.bar(x - width / 2, [normal_ranges[label][0] for label in labels], width, label='Normal Min', color=colors[0])
    ax.bar(x - width / 2, [normal_ranges[label][1] for label in labels], width, bottom=[normal_ranges[label][0] for label in labels], label='Normal Max', color=colors[1])
    ax.bar(x + width / 2, current_values, width, label='Current Value', color=colors[2])

    ax.set_xlabel('Parameters')
    ax.set_ylabel('Values')
    ax.set_title('ECG Parameters Comparison')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()
    ax.set_facecolor('cyan')
    plt.yscale('linear')
    fig.tight_layout()

    graph_path = os.path.join(settings.STATICFILES_DIRS[0], 'images', 'graph.png')
    plt.savefig(graph_path)
    plt.close()

    return graph_path

    
def generate_lft_graph(result_data, current_values):
    labels = ['Bilirubin Total', 'Bilirubin Direct', 'Bilirubin Indirect', 'SGPT', 'SGOT', 'Alkaline Phosphatase']
    normal_ranges = {
        'Bilirubin Total': (0.3, 1.2),
        'Bilirubin Direct': (0.1, 0.3),
        'Bilirubin Indirect': (0.2, 1.0),
        'SGPT': (8, 42),
        'SGOT': (7, 35),
        'Alkaline Phosphatase': (44, 147)
    }

    x = np.arange(len(labels))
    width = 0.35
    colors = ['royalblue', 'green', 'red']
    fig, ax = plt.subplots(figsize=(10, 7), facecolor='lightgreen')
    ax.bar(x - width / 2, [normal_ranges[label][0] for label in labels], width, label='Normal Min', color=colors[0])
    ax.bar(x - width / 2, [normal_ranges[label][1] for label in labels], width, bottom=[normal_ranges[label][0] for label in labels], label='Normal Max', color=colors[1])
    ax.bar(x + width / 2, current_values, width, label='Current Value', color=colors[2])

    ax.set_xlabel('Parameters')
    ax.set_ylabel('Values')
    ax.set_title('Liver Function Test Parameters Comparison')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()
    ax.set_facecolor('lightblue')
    plt.yscale('linear')
    fig.tight_layout()

    graph_path = os.path.join(settings.STATICFILES_DIRS[0], 'images', 'graph.png')
    plt.savefig(graph_path)
    plt.close()

    return graph_path


def generate_kft_graph(result_data, current_values):
    labels = ['Urea', 'Creatinine', 'Uric Acid', 'Sodium', 'Potassium', 'Chloride']
    normal_ranges = {
        'Urea': (15, 45),
        'Creatinine': (0.7, 1.3),
        'Uric Acid': (2.4, 6.0),
        'Sodium': (135, 145),
        'Potassium': (3.5, 5.0),
        'Chloride': (98, 106)
    }

    x = np.arange(len(labels))
    width = 0.35
    colors = ['royalblue', 'green', 'red']
    fig, ax = plt.subplots(figsize=(10, 7), facecolor='lightyellow')
    ax.bar(x - width / 2, [normal_ranges[label][0] for label in labels], width, label='Normal Min', color=colors[0])
    ax.bar(x - width / 2, [normal_ranges[label][1] for label in labels], width, bottom=[normal_ranges[label][0] for label in labels], label='Normal Max', color=colors[1])
    ax.bar(x + width / 2, current_values, width, label='Current Value', color=colors[2])

    ax.set_xlabel('Parameters')
    ax.set_ylabel('Values')
    ax.set_title('Kidney Function Test Parameters Comparison')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()
    ax.set_facecolor('lightpink')
    plt.yscale('linear')
    fig.tight_layout()

    graph_path = os.path.join(settings.STATICFILES_DIRS[0], 'images', 'graph.png')
    plt.savefig(graph_path)
    plt.close()

    return graph_path
