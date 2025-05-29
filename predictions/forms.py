from django import forms

class BPPredictionForm(forms.Form):
    age = forms.IntegerField(min_value=1, max_value=120, label="Age", widget=forms.NumberInput(attrs={'class': 'form-control'}))
    systolic = forms.IntegerField(min_value=50, max_value=250, label="Systolic Pressure (mmHg)", widget=forms.NumberInput(attrs={'class': 'form-control'}))
    diastolic = forms.IntegerField(min_value=30, max_value=150, label="Diastolic Pressure (mmHg)", widget=forms.NumberInput(attrs={'class': 'form-control'}))
    heart_rate = forms.IntegerField(min_value=40, max_value=200, label="Heart Rate (bpm)", widget=forms.NumberInput(attrs={'class': 'form-control'}))
    weight = forms.FloatField(min_value=20, max_value=250, label="Weight (kg)", widget=forms.NumberInput(attrs={'class': 'form-control'}))
    height = forms.FloatField(min_value=100, max_value=250, label="Height (cm)", widget=forms.NumberInput(attrs={'class': 'form-control'}))
    
class CancerPredictionForm(forms.Form):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female')
    ]
    age = forms.IntegerField(min_value=1, max_value=120, label="Age", widget=forms.NumberInput(attrs={'class': 'form-control'}))
    gender = forms.ChoiceField(choices=GENDER_CHOICES, label="Gender", widget=forms.Select(attrs={'class': 'form-control'}))
    pain_level = forms.IntegerField(min_value=0, max_value=10, label="Pain Level (0-10)", widget=forms.NumberInput(attrs={'class': 'form-control'}))
    fatigue = forms.IntegerField(min_value=0, max_value=10, label="Fatigue Level (0-10)", widget=forms.NumberInput(attrs={'class': 'form-control'}))
    weight_loss = forms.BooleanField(required=False, label="Unexplained Weight Loss", widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    smoking = forms.BooleanField(required=False, label="Smoking History", widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))

class ThyroidPredictionForm(forms.Form):
    age = forms.IntegerField(min_value=1, max_value=120, label="Age", widget=forms.NumberInput(attrs={'class': 'form-control'}))
    tsh = forms.FloatField(min_value=0, max_value=100, label="TSH Level (mIU/L)", widget=forms.NumberInput(attrs={'class': 'form-control'}))
    t3 = forms.FloatField(min_value=0, max_value=10, label="T3 Level (nmol/L)", widget=forms.NumberInput(attrs={'class': 'form-control'}))
    t4 = forms.FloatField(min_value=0, max_value=30, label="T4 Level (µg/dL)", widget=forms.NumberInput(attrs={'class': 'form-control'}))
    weight_change = forms.BooleanField(required=False, label="Recent Weight Change", widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    fatigue = forms.BooleanField(required=False, label="Unusual Fatigue", widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))

class AsthmaForm(forms.Form):
    age = forms.IntegerField(min_value=1, max_value=120, label="Age", widget=forms.NumberInput(attrs={'class': 'form-control'}))
    shortness_of_breath = forms.IntegerField(min_value=0, max_value=10, label="Shortness of Breath (0-10)", widget=forms.NumberInput(attrs={'class': 'form-control'}))
    wheezing = forms.IntegerField(min_value=0, max_value=10, label="Wheezing (0-10)", widget=forms.NumberInput(attrs={'class': 'form-control'}))
    coughing = forms.IntegerField(min_value=0, max_value=10, label="Coughing (0-10)", widget=forms.NumberInput(attrs={'class': 'form-control'}))
    chest_tightness = forms.IntegerField(min_value=0, max_value=10, label="Chest Tightness (0-10)", widget=forms.NumberInput(attrs={'class': 'form-control'}))
    family_history = forms.BooleanField(required=False, label="Family History of Asthma", widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))

class LungDiseaseForm(forms.Form):
    age = forms.IntegerField(min_value=1, max_value=120, label="Age", widget=forms.NumberInput(attrs={'class': 'form-control'}))
    smoking_years = forms.IntegerField(min_value=0, max_value=100, label="Years of Smoking", widget=forms.NumberInput(attrs={'class': 'form-control'}))
    cough_duration = forms.IntegerField(min_value=0, max_value=365, label="Cough Duration (days)", widget=forms.NumberInput(attrs={'class': 'form-control'}))
    shortness_of_breath = forms.IntegerField(min_value=0, max_value=10, label="Shortness of Breath (0-10)", widget=forms.NumberInput(attrs={'class': 'form-control'}))
    chest_pain = forms.BooleanField(required=False, label="Chest Pain", widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    fatigue = forms.IntegerField(min_value=0, max_value=10, label="Fatigue Level (0-10)", widget=forms.NumberInput(attrs={'class': 'form-control'}))

class DiabetesForm(forms.Form):
    age = forms.IntegerField(min_value=1, max_value=120, label="Age", widget=forms.NumberInput(attrs={'class': 'form-control'}))
    glucose = forms.FloatField(min_value=50, max_value=300, label="Glucose Level (mg/dL)", widget=forms.NumberInput(attrs={'class': 'form-control'}))
    insulin = forms.FloatField(min_value=0, max_value=300, label="Insulin Level (µU/mL)", widget=forms.NumberInput(attrs={'class': 'form-control'}))
    bmi = forms.FloatField(min_value=10, max_value=50, label="BMI", widget=forms.NumberInput(attrs={'class': 'form-control'}))
    family_history = forms.BooleanField(required=False, label="Family History of Diabetes", widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    physical_activity = forms.IntegerField(min_value=0, max_value=10, label="Physical Activity Level (0-10)", widget=forms.NumberInput(attrs={'class': 'form-control'}))

class KidneyStoneForm(forms.Form):
    age = forms.IntegerField(min_value=1, max_value=120, label="Age", widget=forms.NumberInput(attrs={'class': 'form-control'}))
    pain_level = forms.IntegerField(min_value=0, max_value=10, label="Pain Level (0-10)", widget=forms.NumberInput(attrs={'class': 'form-control'}))
    blood_in_urine = forms.BooleanField(required=False, label="Blood in Urine", widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    nausea = forms.BooleanField(required=False, label="Nausea or Vomiting", widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    fever = forms.FloatField(min_value=35, max_value=42, label="Body Temperature (°C)", widget=forms.NumberInput(attrs={'class': 'form-control'}))
    prior_stones = forms.BooleanField(required=False, label="Prior Kidney Stones", widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))

class LiverDiseaseForm(forms.Form):
    age = forms.IntegerField(min_value=1, max_value=120, label="Age", widget=forms.NumberInput(attrs={'class': 'form-control'}))
    bilirubin = forms.FloatField(min_value=0, max_value=30, label="Total Bilirubin", widget=forms.NumberInput(attrs={'class': 'form-control'}))
    albumin = forms.FloatField(min_value=1, max_value=6, label="Albumin (g/dL)", widget=forms.NumberInput(attrs={'class': 'form-control'}))
    alkaline_phosphatase = forms.FloatField(min_value=20, max_value=500, label="Alkaline Phosphatase (U/L)", widget=forms.NumberInput(attrs={'class': 'form-control'}))
    sgpt = forms.FloatField(min_value=1, max_value=300, label="SGPT (U/L)", widget=forms.NumberInput(attrs={'class': 'form-control'}))
    sgot = forms.FloatField(min_value=1, max_value=300, label="SGOT (U/L)", widget=forms.NumberInput(attrs={'class': 'form-control'}))