"""
Simplified prediction models for demonstration purposes only.
In a real application, these would be trained machine learning models
based on substantial medical data and developed by healthcare professionals.
"""

import random
import numpy as np
from sklearn.linear_model import LogisticRegression


# Note: These are simplified models for demonstration only
# DO NOT use for actual medical diagnoses

def blood_pressure_prediction(age, systolic, diastolic, heart_rate, weight, height):
    """Simplified BP prediction model"""
    # High BP if systolic > 140 or diastolic > 90
    # This is a simplified rule and not for medical use
    has_hypertension = False
    
    if systolic >= 140 or diastolic >= 90:
        probability = 0.7 + (random.random() * 0.3)  # 70-100% chance
        has_hypertension = random.random() < probability
    else:
        probability = 0.0 + (random.random() * 0.3)  # 0-30% chance
        has_hypertension = random.random() < probability
    
    return has_hypertension


def cancer_prediction(age, gender, pain_level, fatigue, weight_loss, smoking):
    """Simplified cancer risk prediction model"""
    # This is a demo model only, not for medical use
    base_risk = 0.1  # base 10% chance
    
    if age > 50:
        base_risk += 0.1
    
    if smoking:
        base_risk += 0.2
    
    if weight_loss:
        base_risk += 0.15
    
    if pain_level > 7:
        base_risk += 0.1
    
    if fatigue > 7:
        base_risk += 0.1
    
    # Add some randomness
    base_risk += (random.random() * 0.2) - 0.1
    
    # Cap between 0 and 1
    base_risk = max(0, min(1, base_risk))
    
    return random.random() < base_risk


def thyroid_prediction(age, tsh, t3, t4, weight_change, fatigue):
    """Simplified thyroid condition prediction"""
    # This is a demo model only, not for medical use
    has_thyroid_issue = False
    
    # Simple rule-based approach (not medically accurate)
    if (tsh < 0.4 or tsh > 4.0) or (t3 < 0.8 or t3 > 2.0) or (t4 < 5 or t4 > 12):
        probability = 0.6 + (random.random() * 0.4)  # 60-100% chance
        if weight_change and fatigue:
            probability += 0.2
        has_thyroid_issue = random.random() < probability
    else:
        probability = 0.0 + (random.random() * 0.2)  # 0-20% chance
        has_thyroid_issue = random.random() < probability
    
    return has_thyroid_issue


def asthma_prediction(age, shortness_of_breath, wheezing, coughing, chest_tightness, family_history):
    """Simplified asthma prediction"""
    # This is a demo model only, not for medical use
    has_asthma = False
    
    # Simple rule-based approach
    total_symptoms = shortness_of_breath + wheezing + coughing + chest_tightness
    
    if total_symptoms > 15:
        probability = 0.7 + (random.random() * 0.3)  # 70-100% chance
        if family_history:
            probability += 0.1
        has_asthma = random.random() < probability
    elif total_symptoms > 10:
        probability = 0.4 + (random.random() * 0.3)  # 40-70% chance
        if family_history:
            probability += 0.1
        has_asthma = random.random() < probability
    else:
        probability = 0.0 + (random.random() * 0.3)  # 0-30% chance
        if family_history:
            probability += 0.1
        has_asthma = random.random() < probability
    
    return has_asthma


def lung_disease_prediction(age, smoking_years, cough_duration, shortness_of_breath, chest_pain, fatigue):
    """Simplified lung disease prediction"""
    # This is a demo model only, not for medical use
    has_lung_disease = False
    
    # Simple rule-based approach
    risk_score = 0
    
    if age > 50:
        risk_score += 1
    
    if smoking_years > 10:
        risk_score += 2
    
    if cough_duration > 21:  # More than 3 weeks
        risk_score += 2
    
    if shortness_of_breath > 5:
        risk_score += 1
    
    if chest_pain:
        risk_score += 1
    
    if fatigue > 7:
        risk_score += 1
    
    # Decision based on risk score
    if risk_score >= 5:
        probability = 0.7 + (random.random() * 0.3)  # 70-100% chance
        has_lung_disease = random.random() < probability
    elif risk_score >= 3:
        probability = 0.3 + (random.random() * 0.4)  # 30-70% chance
        has_lung_disease = random.random() < probability
    else:
        probability = 0.0 + (random.random() * 0.2)  # 0-20% chance
        has_lung_disease = random.random() < probability
    
    return has_lung_disease


def diabetes_prediction(age, glucose, insulin, bmi, family_history, physical_activity):
    """Simplified diabetes prediction"""
    # This is a demo model only, not for medical use
    has_diabetes = False
    
    # Simple rule-based approach
    if glucose > 126:  # Fasting glucose > 126 mg/dL is a diabetes indicator
        probability = 0.7 + (random.random() * 0.3)  # 70-100% chance
        if bmi > 30:  # Obesity increases risk
            probability += 0.1
        if family_history:
            probability += 0.1
        if physical_activity < 3:  # Low physical activity increases risk
            probability += 0.1
        has_diabetes = random.random() < probability
    elif glucose > 100:  # 100-125 mg/dL is prediabetic range
        probability = 0.3 + (random.random() * 0.4)  # 30-70% chance
        if bmi > 30:
            probability += 0.1
        if family_history:
            probability += 0.1
        if physical_activity < 3:
            probability += 0.1
        has_diabetes = random.random() < probability
    else:
        probability = 0.0 + (random.random() * 0.2)  # 0-20% chance
        if bmi > 30:
            probability += 0.1
        if family_history:
            probability += 0.1
        has_diabetes = random.random() < probability
    
    return has_diabetes


def kidney_stone_prediction(age, pain_level, blood_in_urine, nausea, fever, prior_stones):
    """Simplified kidney stone prediction"""
    # This is a demo model only, not for medical use
    has_kidney_stone = False
    
    # Simple rule-based approach
    risk_score = 0
    
    if pain_level > 7:  # Severe pain
        risk_score += 2
    
    if blood_in_urine:
        risk_score += 2
    
    if nausea:
        risk_score += 1
    
    if fever > 38:  # Fever above 38°C
        risk_score += 1
    
    if prior_stones:
        risk_score += 2
    
    # Decision based on risk score
    if risk_score >= 5:
        probability = 0.8 + (random.random() * 0.2)  # 80-100% chance
        has_kidney_stone = random.random() < probability
    elif risk_score >= 3:
        probability = 0.4 + (random.random() * 0.4)  # 40-80% chance
        has_kidney_stone = random.random() < probability
    else:
        probability = 0.0 + (random.random() * 0.3)  # 0-30% chance
        has_kidney_stone = random.random() < probability
    
    return has_kidney_stone


def liver_disease_prediction(age, bilirubin, albumin, alkaline_phosphatase, sgpt, sgot):
    """Simplified liver disease prediction"""
    # This is a demo model only, not for medical use
    has_liver_disease = False
    
    # Simple rule-based approach (not medically accurate)
    risk_score = 0
    
    if bilirubin > 1.2:  # High bilirubin
        risk_score += 2
    
    if albumin < 3.5:  # Low albumin
        risk_score += 2
    
    if alkaline_phosphatase > 120:  # High alkaline phosphatase
        risk_score += 1
    
    if sgpt > 40:  # High SGPT (ALT)
        risk_score += 2
    
    if sgot > 40:  # High SGOT (AST)
        risk_score += 2
    
    # Decision based on risk score
    if risk_score >= 6:
        probability = 0.8 + (random.random() * 0.2)  # 80-100% chance
        has_liver_disease = random.random() < probability
    elif risk_score >= 4:
        probability = 0.5 + (random.random() * 0.3)  # 50-80% chance
        has_liver_disease = random.random() < probability
    elif risk_score >= 2:
        probability = 0.2 + (random.random() * 0.3)  # 20-50% chance
        has_liver_disease = random.random() < probability
    else:
        probability = 0.0 + (random.random() * 0.1)  # 0-10% chance
        has_liver_disease = random.random() < probability
    
    return has_liver_disease