

import os
import numpy as np
import matplotlib.pyplot as plt
from django.conf import settings
from .forms import BloodTestForm, ECGForm, LFTForm, KFTForm

def convert_blood_test_data(form_data):
    hemoglobin = form_data['hemoglobin']
    white_blood_cells = form_data['white_blood_cells']
    platelets = form_data['platelets']
    red_blood_cells = form_data['red_blood_cells']
    hematocrit = form_data['hematocrit']
    glucose = form_data['glucose']

    result_data = []

    if hemoglobin < 13.5:
        result_data.append(('Hemoglobin', 'Insufficient (Below normal)', 'insufficient'))
    elif hemoglobin > 17.5:
        result_data.append(('Hemoglobin', 'High (Above normal)', 'high'))
    else:
        result_data.append(('Hemoglobin', 'Within normal range', 'normal'))

    if white_blood_cells < 4.5:
        result_data.append(('White Blood Cells', 'Low (Below normal)', 'low'))
    elif white_blood_cells > 11.0:
        result_data.append(('White Blood Cells', 'High (Above normal)', 'high'))
    else:
        result_data.append(('White Blood Cells', 'Within normal range', 'normal'))

    if platelets < 150:
        result_data.append(('Platelets', 'Very Low (Critical)', 'critical'))
    elif platelets < 180:
        result_data.append(('Platelets', 'Low (Needs monitoring)', 'low'))
    elif platelets > 450:
        result_data.append(('Platelets', 'High (May require monitoring)', 'high'))
    else:
        result_data.append(('Platelets', 'Within normal range', 'normal'))

    if red_blood_cells < 4.7:
        result_data.append(('Red Blood Cells', 'Low (Below normal)', 'low'))
    elif red_blood_cells > 6.1:
        result_data.append(('Red Blood Cells', 'High (Above normal)', 'high'))
    else:
        result_data.append(('Red Blood Cells', 'Within normal range', 'normal'))

    if hematocrit < 40:
        result_data.append(('Hematocrit', 'Low (Below normal)', 'low'))
    elif hematocrit > 52:
        result_data.append(('Hematocrit', 'High (Above normal)', 'high'))
    else:
        result_data.append(('Hematocrit', 'Within normal range', 'normal'))

    if glucose < 70:
        result_data.append(('Glucose', 'Low (Below normal)', 'low'))
    elif glucose > 140:
        result_data.append(('Glucose', 'High (Above normal)', 'high'))
    else:
        result_data.append(('Glucose', 'Within normal range', 'normal'))

    return result_data, (hemoglobin, white_blood_cells, platelets, red_blood_cells, hematocrit, glucose)


def convert_ecg_data(form_data):
    heart_rate = form_data['heart_rate']
    pr_interval = form_data['pr_interval']
    qrs_duration = form_data['qrs_duration']
    qt_interval = form_data['qt_interval']

    result_data = []

    if heart_rate < 60:
        result_data.append(('Heart Rate', 'Low (Bradycardia)', 'low'))
    elif heart_rate > 100:
        result_data.append(('Heart Rate', 'High (Tachycardia)', 'high'))
    else:
        result_data.append(('Heart Rate', 'Normal', 'normal'))

    if pr_interval < 120:
        result_data.append(('PR Interval', 'Shortened (Possible AV Node Conduction Issue)', 'low'))
    elif pr_interval > 200:
        result_data.append(('PR Interval', 'Prolonged (Possible Heart Block)', 'high'))
    else:
        result_data.append(('PR Interval', 'Normal', 'normal'))

    if qrs_duration < 80:
        result_data.append(('QRS Duration', 'Short (Possible Bundle Branch Block)', 'low'))
    elif qrs_duration > 120:
        result_data.append(('QRS Duration', 'Prolonged (Possible Conduction Delay)', 'high'))
    else:
        result_data.append(('QRS Duration', 'Normal', 'normal'))

    qt_corrected = qt_interval / np.sqrt(heart_rate / 60)
    if qt_corrected > 440:
        result_data.append(('QTc Interval', 'Prolonged (Risk of Arrhythmias)', 'high'))
    elif qt_corrected < 340:
        result_data.append(('QTc Interval', 'Short (Possible Hypercalcemia)', 'low'))
    else:
        result_data.append(('QTc Interval', 'Normal', 'normal'))

    return result_data, (heart_rate, pr_interval, qrs_duration, qt_interval)



def convert_lft_data(form_data):
    bilirubin_total = form_data['bilirubin_total']
    bilirubin_direct = form_data['bilirubin_direct']
    bilirubin_indirect = form_data['bilirubin_indirect']
    sgpt = form_data['sgpt']
    sgot = form_data['sgot']
    alkaline_phosphatase = form_data['alkaline_phosphatase']

    result_data = []

    if bilirubin_total < 0.3:
        result_data.append(('Bilirubin Total', 'Low (Below normal)', 'low'))
    elif bilirubin_total > 1.2:
        result_data.append(('Bilirubin Total', 'High (Above normal)', 'high'))
    else:
        result_data.append(('Bilirubin Total', 'Within normal range', 'normal'))

    if bilirubin_direct > 0.3:
        result_data.append(('Bilirubin Direct', 'High (Above normal)', 'high'))
    else:
        result_data.append(('Bilirubin Direct', 'Within normal range', 'normal'))

    if bilirubin_indirect > 1.0:
        result_data.append(('Bilirubin Indirect', 'High (Above normal)', 'high'))
    else:
        result_data.append(('Bilirubin Indirect', 'Within normal range', 'normal'))

    if sgpt < 8:
        result_data.append(('SGPT', 'Low (Below normal)', 'low'))
    elif sgpt > 42:
        result_data.append(('SGPT', 'High (Above normal)', 'high'))
    else:
        result_data.append(('SGPT', 'Within normal range', 'normal'))

    if sgot < 7:
        result_data.append(('SGOT', 'Low (Below normal)', 'low'))
    elif sgot > 35:
        result_data.append(('SGOT', 'High (Above normal)', 'high'))
    else:
        result_data.append(('SGOT', 'Within normal range', 'normal'))

    if alkaline_phosphatase < 44:
        result_data.append(('Alkaline Phosphatase', 'Low (Below normal)', 'low'))
    elif alkaline_phosphatase > 147:
        result_data.append(('Alkaline Phosphatase', 'High (Above normal)', 'high'))
    else:
        result_data.append(('Alkaline Phosphatase', 'Within normal range', 'normal'))

    return result_data, (bilirubin_total, bilirubin_direct, bilirubin_indirect, sgpt, sgot, alkaline_phosphatase)


def convert_kft_data(form_data):
    urea = form_data['urea']
    creatinine = form_data['creatinine']
    uric_acid = form_data['uric_acid']
    sodium = form_data['sodium']
    potassium = form_data['potassium']
    chloride = form_data['chloride']

    result_data = []

    if urea < 15:
        result_data.append(('Urea', 'Low (Below normal)', 'low'))
    elif urea > 45:
        result_data.append(('Urea', 'High (Above normal)', 'high'))
    else:
        result_data.append(('Urea', 'Within normal range', 'normal'))

    if creatinine < 0.7:
        result_data.append(('Creatinine', 'Low (Below normal)', 'low'))
    elif creatinine > 1.3:
        result_data.append(('Creatinine', 'High (Above normal)', 'high'))
    else:
        result_data.append(('Creatinine', 'Within normal range', 'normal'))

    if uric_acid < 2.4:
        result_data.append(('Uric Acid', 'Low (Below normal)', 'low'))
    elif uric_acid > 6.0:
        result_data.append(('Uric Acid', 'High (Above normal)', 'high'))
    else:
        result_data.append(('Uric Acid', 'Within normal range', 'normal'))

    if sodium < 135:
        result_data.append(('Sodium', 'Low (Below normal)', 'low'))
    elif sodium > 145:
        result_data.append(('Sodium', 'High (Above normal)', 'high'))
    else:
        result_data.append(('Sodium', 'Within normal range', 'normal'))

    if potassium < 3.5:
        result_data.append(('Potassium', 'Low (Below normal)', 'low'))
    elif potassium > 5.0:
        result_data.append(('Potassium', 'High (Above normal)', 'high'))
    else:
        result_data.append(('Potassium', 'Within normal range', 'normal'))

    if chloride < 98:
        result_data.append(('Chloride', 'Low (Below normal)', 'low'))
    elif chloride > 106:
        result_data.append(('Chloride', 'High (Above normal)', 'high'))
    else:
        result_data.append(('Chloride', 'Within normal range', 'normal'))

    return result_data, (urea, creatinine, uric_acid, sodium, potassium, chloride)
