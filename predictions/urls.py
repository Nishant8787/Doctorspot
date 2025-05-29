from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('predict/bp/', views.predict_bp, name='predict_bp'),
    path('predict/cancer/', views.predict_cancer, name='predict_cancer'),
    path('predict/thyroid/', views.predict_thyroid, name='predict_thyroid'),
    path('predict/asthma/', views.predict_asthma, name='predict_asthma'),
    path('predict/lung/', views.predict_lung, name='predict_lung'),
    path('predict/diabetes/', views.predict_diabetes, name='predict_diabetes'),
    path('predict/kidney/', views.predict_kidney, name='predict_kidney'),
    path('predict/liver/', views.predict_liver, name='predict_liver'),
    path('history/', views.prediction_history, name='prediction_history'),
]