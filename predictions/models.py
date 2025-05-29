from django.db import models
from django.contrib.auth.models import User


class PredictionHistory(models.Model):
    DISEASE_CHOICES = [
        ('BP', 'Blood Pressure'),
        ('Cancer', 'Cancer'),
        ('Thyroid', 'Thyroid'),
        ('Asthma', 'Asthma'),
        ('Lung', 'Lung Disease'),
        ('Diabetes', 'Diabetes'),
        ('Kidney', 'Kidney Stone'),
        ('Liver', 'Liver Disease'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    disease_type = models.CharField(max_length=20, choices=DISEASE_CHOICES)
    parameters = models.JSONField()
    result = models.BooleanField()  # True if disease detected, False otherwise
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.get_disease_type_display()} - {self.created_at.strftime('%Y-%m-%d %H:%M')}"
    
    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "Prediction histories"