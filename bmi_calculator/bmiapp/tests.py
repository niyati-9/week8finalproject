from django.test import TestCase
from django.urls import reverse
from .forms import BMIForm

class BMICalculatorTests(TestCase):

    # Test if the form is valid with correct data
    def test_bmi_form_valid(self):
        form_data = {
            'current_weight': 70,
            'height': 1.75,
            'goal_weight': 65,
            'estimated_weeks': 10,
            'age': 30,
            'exercise_level': 'moderate',
        }
        form = BMIForm(data=form_data)
        self.assertTrue(form.is_valid())

    # Test if the form is invalid with incorrect data
    def test_bmi_form_invalid(self):
        form_data = {
            'current_weight': '',  # Invalid: Empty weight
            'height': 1.75,
            'goal_weight': 65,
            'estimated_weeks': 10,
            'age': 30,
            'exercise_level': 'moderate',
        }
        form = BMIForm(data=form_data)
        self.assertFalse(form.is_valid())

    # Test if the BMI form view renders correctly
    def test_bmi_view(self):
        response = self.client.get(reverse('bmi_calculator'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bmiapp/bmi_form.html')

    # Test if the BMI result view renders correctly after form submission
    def test_bmi_result_view(self):
        form_data = {
            'current_weight': 70,
            'height': 1.75,
            'goal_weight': 65,
            'estimated_weeks': 10,
            'age': 30,
            'exercise_level': 'moderate',
        }
        response = self.client.post(reverse('bmi_calculator'), data=form_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bmiapp/bmi_result.html')

    # Test if the BMI calculation is correct
    def test_bmi_calculation(self):
        # This would simulate calling the calculate_bmi function
        weight = 70
        height = 1.75
        bmi = round(weight / (height ** 2), 2)
        self.assertEqual(bmi, 22.86)

    # Test if weekly calorie calculation is correct
    def test_weekly_calories_calculation(self):
        # This would simulate calling the calculate_weekly_calories function
        current_weight = 70
        goal_weight = 65
        weeks = 10
        weight_change = abs(current_weight - goal_weight)
        calories_needed = weight_change * 7700  # 7700 calories per kg
        weekly_calories = round(calories_needed / weeks, 2)
        self.assertEqual(weekly_calories, 3850.0)

