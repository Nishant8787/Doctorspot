from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import (
    BPPredictionForm, CancerPredictionForm, ThyroidPredictionForm,
    AsthmaForm, LungDiseaseForm, DiabetesForm, KidneyStoneForm, LiverDiseaseForm
)
from .models import PredictionHistory
from .predictors import (
    blood_pressure_prediction, cancer_prediction, thyroid_prediction,
    asthma_prediction, lung_disease_prediction, diabetes_prediction,
    kidney_stone_prediction, liver_disease_prediction
)


def home(request):
    """Home page view"""
    return render(request, 'predictions/home.html')


@login_required
def predict_bp(request):
    """Blood pressure prediction view"""
    result = None
    if request.method == 'POST':
        form = BPPredictionForm(request.POST)
        if form.is_valid():
            # Extract data from form
            age = form.cleaned_data['age']
            systolic = form.cleaned_data['systolic']
            diastolic = form.cleaned_data['diastolic']
            heart_rate = form.cleaned_data['heart_rate']
            weight = form.cleaned_data['weight']
            height = form.cleaned_data['height']
            
            # Make prediction
            result = blood_pressure_prediction(age, systolic, diastolic, heart_rate, weight, height)
            
            # Save prediction to history
            PredictionHistory.objects.create(
                user=request.user,
                disease_type='BP',
                parameters={
                    'age': age,
                    'systolic': systolic,
                    'diastolic': diastolic,
                    'heart_rate': heart_rate,
                    'weight': weight,
                    'height': height
                },
                result=result
            )
    else:
        form = BPPredictionForm()
    
    return render(request, 'predictions/predict_bp.html', {
        'form': form,
        'result': result,
        'title': 'Blood Pressure Prediction'
    })


@login_required
def predict_cancer(request):
    """Cancer prediction view"""
    result = None
    if request.method == 'POST':
        form = CancerPredictionForm(request.POST)
        if form.is_valid():
            # Extract data
            age = form.cleaned_data['age']
            gender = form.cleaned_data['gender']
            pain_level = form.cleaned_data['pain_level']
            fatigue = form.cleaned_data['fatigue']
            weight_loss = form.cleaned_data['weight_loss']
            smoking = form.cleaned_data['smoking']
            
            # Make prediction
            result = cancer_prediction(age, gender, pain_level, fatigue, weight_loss, smoking)
            
            # Save to history
            PredictionHistory.objects.create(
                user=request.user,
                disease_type='Cancer',
                parameters={
                    'age': age,
                    'gender': gender,
                    'pain_level': pain_level,
                    'fatigue': fatigue,
                    'weight_loss': weight_loss,
                    'smoking': smoking
                },
                result=result
            )
    else:
        form = CancerPredictionForm()
    
    return render(request, 'predictions/predict_cancer.html', {
        'form': form,
        'result': result,
        'title': 'Cancer Risk Prediction'
    })


@login_required
def predict_thyroid(request):
    """Thyroid prediction view"""
    result = None
    if request.method == 'POST':
        form = ThyroidPredictionForm(request.POST)
        if form.is_valid():
            # Extract data
            age = form.cleaned_data['age']
            tsh = form.cleaned_data['tsh']
            t3 = form.cleaned_data['t3']
            t4 = form.cleaned_data['t4']
            weight_change = form.cleaned_data['weight_change']
            fatigue = form.cleaned_data['fatigue']
            
            # Make prediction
            result = thyroid_prediction(age, tsh, t3, t4, weight_change, fatigue)
            
            # Save to history
            PredictionHistory.objects.create(
                user=request.user,
                disease_type='Thyroid',
                parameters={
                    'age': age,
                    'tsh': tsh,
                    't3': t3,
                    't4': t4,
                    'weight_change': weight_change,
                    'fatigue': fatigue
                },
                result=result
            )
    else:
        form = ThyroidPredictionForm()
    
    return render(request, 'predictions/predict_thyroid.html', {
        'form': form,
        'result': result,
        'title': 'Thyroid Condition Prediction'
    })


@login_required
def predict_asthma(request):
    """Asthma prediction view"""
    result = None
    if request.method == 'POST':
        form = AsthmaForm(request.POST)
        if form.is_valid():
            # Extract data
            age = form.cleaned_data['age']
            shortness_of_breath = form.cleaned_data['shortness_of_breath']
            wheezing = form.cleaned_data['wheezing']
            coughing = form.cleaned_data['coughing']
            chest_tightness = form.cleaned_data['chest_tightness']
            family_history = form.cleaned_data['family_history']
            
            # Make prediction
            result = asthma_prediction(age, shortness_of_breath, wheezing, coughing, chest_tightness, family_history)
            
            # Save to history
            PredictionHistory.objects.create(
                user=request.user,
                disease_type='Asthma',
                parameters={
                    'age': age,
                    'shortness_of_breath': shortness_of_breath,
                    'wheezing': wheezing,
                    'coughing': coughing,
                    'chest_tightness': chest_tightness,
                    'family_history': family_history
                },
                result=result
            )
    else:
        form = AsthmaForm()
    
    return render(request, 'predictions/predict_asthma.html', {
        'form': form,
        'result': result,
        'title': 'Asthma Prediction'
    })


@login_required
def predict_lung(request):
    """Lung disease prediction view"""
    result = None
    if request.method == 'POST':
        form = LungDiseaseForm(request.POST)
        if form.is_valid():
            # Extract data
            age = form.cleaned_data['age']
            smoking_years = form.cleaned_data['smoking_years']
            cough_duration = form.cleaned_data['cough_duration']
            shortness_of_breath = form.cleaned_data['shortness_of_breath']
            chest_pain = form.cleaned_data['chest_pain']
            fatigue = form.cleaned_data['fatigue']
            
            # Make prediction
            result = lung_disease_prediction(age, smoking_years, cough_duration, shortness_of_breath, chest_pain, fatigue)
            
            # Save to history
            PredictionHistory.objects.create(
                user=request.user,
                disease_type='Lung',
                parameters={
                    'age': age,
                    'smoking_years': smoking_years,
                    'cough_duration': cough_duration,
                    'shortness_of_breath': shortness_of_breath,
                    'chest_pain': chest_pain,
                    'fatigue': fatigue
                },
                result=result
            )
    else:
        form = LungDiseaseForm()
    
    return render(request, 'predictions/predict_lung.html', {
        'form': form,
        'result': result,
        'title': 'Lung Disease Prediction'
    })


@login_required
def predict_diabetes(request):
    """Diabetes prediction view"""
    result = None
    if request.method == 'POST':
        form = DiabetesForm(request.POST)
        if form.is_valid():
            # Extract data
            age = form.cleaned_data['age']
            glucose = form.cleaned_data['glucose']
            insulin = form.cleaned_data['insulin']
            bmi = form.cleaned_data['bmi']
            family_history = form.cleaned_data['family_history']
            physical_activity = form.cleaned_data['physical_activity']
            
            # Make prediction
            result = diabetes_prediction(age, glucose, insulin, bmi, family_history, physical_activity)
            
            # Save to history
            PredictionHistory.objects.create(
                user=request.user,
                disease_type='Diabetes',
                parameters={
                    'age': age,
                    'glucose': glucose,
                    'insulin': insulin,
                    'bmi': bmi,
                    'family_history': family_history,
                    'physical_activity': physical_activity
                },
                result=result
            )
    else:
        form = DiabetesForm()
    
    return render(request, 'predictions/predict_diabetes.html', {
        'form': form,
        'result': result,
        'title': 'Diabetes Prediction'
    })


@login_required
def predict_kidney(request):
    """Kidney stone prediction view"""
    result = None
    if request.method == 'POST':
        form = KidneyStoneForm(request.POST)
        if form.is_valid():
            # Extract data
            age = form.cleaned_data['age']
            pain_level = form.cleaned_data['pain_level']
            blood_in_urine = form.cleaned_data['blood_in_urine']
            nausea = form.cleaned_data['nausea']
            fever = form.cleaned_data['fever']
            prior_stones = form.cleaned_data['prior_stones']
            
            # Make prediction
            result = kidney_stone_prediction(age, pain_level, blood_in_urine, nausea, fever, prior_stones)
            
            # Save to history
            PredictionHistory.objects.create(
                user=request.user,
                disease_type='Kidney',
                parameters={
                    'age': age,
                    'pain_level': pain_level,
                    'blood_in_urine': blood_in_urine,
                    'nausea': nausea,
                    'fever': fever,
                    'prior_stones': prior_stones
                },
                result=result
            )
    else:
        form = KidneyStoneForm()
    
    return render(request, 'predictions/predict_kidney.html', {
        'form': form,
        'result': result,
        'title': 'Kidney Stone Prediction'
    })


@login_required
def predict_liver(request):
    """Liver disease prediction view"""
    result = None
    if request.method == 'POST':
        form = LiverDiseaseForm(request.POST)
        if form.is_valid():
            # Extract data
            age = form.cleaned_data['age']
            bilirubin = form.cleaned_data['bilirubin']
            albumin = form.cleaned_data['albumin']
            alkaline_phosphatase = form.cleaned_data['alkaline_phosphatase']
            sgpt = form.cleaned_data['sgpt']
            sgot = form.cleaned_data['sgot']
            
            # Make prediction
            result = liver_disease_prediction(age, bilirubin, albumin, alkaline_phosphatase, sgpt, sgot)
            
            # Save to history
            PredictionHistory.objects.create(
                user=request.user,
                disease_type='Liver',
                parameters={
                    'age': age,
                    'bilirubin': bilirubin,
                    'albumin': albumin,
                    'alkaline_phosphatase': alkaline_phosphatase,
                    'sgpt': sgpt,
                    'sgot': sgot
                },
                result=result
            )
    else:
        form = LiverDiseaseForm()
    
    return render(request, 'predictions/predict_liver.html', {
        'form': form,
        'result': result,
        'title': 'Liver Disease Prediction'
    })


@login_required
def prediction_history(request):
    """View user's prediction history"""
    history = PredictionHistory.objects.filter(user=request.user)
    return render(request, 'predictions/history.html', {'history': history})