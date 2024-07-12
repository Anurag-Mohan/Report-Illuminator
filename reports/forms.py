from django import forms

class BloodTestForm(forms.Form):
    hemoglobin = forms.FloatField(label='Hemoglobin', widget=forms.NumberInput(attrs={'class': 'form-control custom-input'}))
    white_blood_cells = forms.FloatField(label='White Blood Cells', widget=forms.NumberInput(attrs={'class': 'form-control custom-input'}))
    platelets = forms.FloatField(label='Platelets', widget=forms.NumberInput(attrs={'class': 'form-control custom-input'}))
    red_blood_cells = forms.FloatField(label='Red Blood Cells (x10^12/L)', widget=forms.NumberInput(attrs={'class': 'form-control custom-input'}))
    hematocrit = forms.FloatField(label='Hematocrit (%)', widget=forms.NumberInput(attrs={'class': 'form-control custom-input'}))
    glucose = forms.FloatField(label='Glucose (mg/dL)', widget=forms.NumberInput(attrs={'class': 'form-control custom-input'}))

class ECGForm(forms.Form):
    heart_rate = forms.IntegerField(label='Heart Rate (bpm)', widget=forms.NumberInput(attrs={'class': 'form-control custom-input'}))
    pr_interval = forms.FloatField(label='PR Interval (ms)', widget=forms.NumberInput(attrs={'class': 'form-control custom-input'}))
    qrs_duration = forms.FloatField(label='QRS Duration (ms)', widget=forms.NumberInput(attrs={'class': 'form-control custom-input'}))
    qt_interval = forms.FloatField(label='QT Interval (ms)', widget=forms.NumberInput(attrs={'class': 'form-control custom-input'}))

class LFTForm(forms.Form):
    bilirubin_total = forms.FloatField(label='Bilirubin Total (mg/dL)', widget=forms.NumberInput(attrs={'class': 'form-control custom-input'}))
    bilirubin_direct = forms.FloatField(label='Bilirubin Direct (mg/dL)', widget=forms.NumberInput(attrs={'class': 'form-control custom-input'}))
    bilirubin_indirect = forms.FloatField(label='Bilirubin Indirect (mg/dL)', widget=forms.NumberInput(attrs={'class': 'form-control custom-input'}))
    sgpt = forms.FloatField(label='SGPT (U/L)', widget=forms.NumberInput(attrs={'class': 'form-control custom-input'}))
    sgot = forms.FloatField(label='SGOT (U/L)', widget=forms.NumberInput(attrs={'class': 'form-control custom-input'}))
    alkaline_phosphatase = forms.FloatField(label='Alkaline Phosphatase (U/L)', widget=forms.NumberInput(attrs={'class': 'form-control custom-input'}))

class KFTForm(forms.Form):
    urea = forms.FloatField(label='Urea (mg/dL)', widget=forms.NumberInput(attrs={'class': 'form-control custom-input'}))
    creatinine = forms.FloatField(label='Creatinine (mg/dL)', widget=forms.NumberInput(attrs={'class': 'form-control custom-input'}))
    uric_acid = forms.FloatField(label='Uric Acid (mg/dL)', widget=forms.NumberInput(attrs={'class': 'form-control custom-input'}))
    sodium = forms.FloatField(label='Sodium (mmol/L)', widget=forms.NumberInput(attrs={'class': 'form-control custom-input'}))
    potassium = forms.FloatField(label='Potassium (mmol/L)', widget=forms.NumberInput(attrs={'class': 'form-control custom-input'}))
    chloride = forms.FloatField(label='Chloride (mmol/L)', widget=forms.NumberInput(attrs={'class': 'form-control custom-input'}))
