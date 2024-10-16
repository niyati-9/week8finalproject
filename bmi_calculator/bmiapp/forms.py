from django import forms

class BMIForm(forms.Form):
    weight = forms.FloatField(label='Weight (kg)')
    height = forms.FloatField(label='Height (m)')
