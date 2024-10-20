from django import forms

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