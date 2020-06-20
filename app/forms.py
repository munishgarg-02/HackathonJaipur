from django import forms
from app import models

class Patient(forms.ModelForm):
    class Meta:
        model = models.PatientDetails
        fields = '__all__'