# bmiapp/forms.py
from django import forms

class BMIForm(forms.Form):
    name = forms.CharField(label="Name", max_length=100)
    height = forms.FloatField(label="Height (in meters)", min_value=0)
    weight = forms.FloatField(label="Weight (in kilograms)", min_value=0)
