from django import forms

class BMICalculatorForm(forms.Form):
    weight = forms.FloatField(label='Weight (kg)', min_value=0)
    height = forms.FloatField(label='Height (m)', min_value=0)
    activity_level = forms.ChoiceField(
        label='Activity Level',
        choices=[
            (1, 'Sedentary'),
            (2, 'Lightly Active'),
            (3, 'Moderately Active'),
            (4, 'Very Active')
        ]
    )
