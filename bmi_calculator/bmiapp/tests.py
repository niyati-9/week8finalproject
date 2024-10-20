from django.test import TestCase
from django.urls import reverse
from .forms import BMIForm
from .views import calculate_bmi


class BMICalculatorTests(TestCase):

    def test_bmi_calculation(self):
        """
        Test BMI calculation logic.
        """
        weight = 70  # kg
        height = 1.75  # meters
        expected_bmi = 22.86  # Expected BMI = 70 / (1.75^2)
        calculated_bmi = calculate_bmi(weight, height)
        self.assertAlmostEqual(calculated_bmi, expected_bmi, places=2)

    def test_bmi_form_valid(self):
        """
        Test if the form is valid with correct data.
        """
        form_data = {
            'current_weight': 70,
            'height': 1.75,
            'goal_weight': 65,
            'estimated_weeks': 10,
            'age': 30,
            'exercise_level': 'Sedentary'
        }
        form = BMIForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_bmi_form_invalid_missing_fields(self):
        """
        Test if the form is invalid when required fields are missing.
        """
        form_data = {
            'current_weight': 70,
            'height': 1.75,
            # 'goal_weight': Missing
            'estimated_weeks': 10,
            'age': 30,
            'exercise_level': 'Sedentary'
        }
        form = BMIForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_bmi_form_invalid_negative_weight(self):
        """
        Test if the form is invalid when negative weight is provided.
        """
        form_data = {
            'current_weight': -70,
            'height': 1.75,
            'goal_weight': 65,
            'estimated_weeks': 10,
            'age': 30,
            'exercise_level': 'Sedentary'
        }
        form = BMIForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_bmi_view(self):
        """
        Test if the BMI form view renders correctly.
        """
        response = self.client.get(reverse('bmi_form'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bmiapp/bmi_form.html')

    def test_bmi_result_view(self):
        """
        Test if the BMI result view renders correctly after form submission.
        """
        form_data = {
            'current_weight': 70,
            'height': 1.75,
            'goal_weight': 65,
            'estimated_weeks': 10,
            'age': 30,
            'exercise_level': 'Sedentary'
        }
        response = self.client.post(reverse('bmi_form'), data=form_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bmiapp/bmi_result.html')


def calculate_bmi(weight, height):
    """
    Helper function to calculate BMI.
    """
    if height <= 0:
        return None
    return round(weight / (height ** 2), 2)
