from django import forms
from django.core.exceptions import ValidationError

EXERCISE_CHOICES = [
    ('sedentary', 'Sedentary (little to no exercise)'),
    ('light', 'Light exercise (1-3 days per week)'),
    ('moderate', 'Moderate exercise (3-5 days per week)'),
    ('active', 'Active (6-7 days per week)'),
    ('very_active', 'Very Active (twice per day)'),
]

class BMIForm(forms.Form):
    current_weight = forms.FloatField(label='Current Weight (kg)')
    height = forms.FloatField(label='Height (m)')
    goal_weight = forms.FloatField(label='Goal Weight (kg)')
    estimated_weeks = forms.IntegerField(label='Estimated Weeks')
    age = forms.IntegerField(label='Age')
    exercise_level = forms.ChoiceField(choices=EXERCISE_CHOICES, label='Exercise Level')

    def clean_current_weight(self):
        weight = self.cleaned_data['current_weight']
        if weight <= 0:
            raise ValidationError("Weight must be greater than 0.")
        return weight

    def clean_height(self):
        height = self.cleaned_data['height']
        if height <= 0:
            raise ValidationError("Height must be greater than 0.")
        return height

    def clean_goal_weight(self):
        weight = self.cleaned_data['goal_weight']
        if weight <= 0:
            raise ValidationError("Goal weight must be greater than 0.")
        return weight

    def clean_estimated_weeks(self):
        weeks = self.cleaned_data['estimated_weeks']
        if weeks <= 0:
            raise ValidationError("Estimated weeks must be greater than 0.")
        return weeks

    def clean_age(self):
        age = self.cleaned_data['age']
        if age <= 0:
            raise ValidationError("Age must be greater than 0.")
        if age > 120:
            raise ValidationError("Please enter a valid age.")
        return age