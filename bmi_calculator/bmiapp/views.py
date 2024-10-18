from django.shortcuts import render
from .forms import BMIForm

def calculate_bmi(weight, height):
    return round(weight / (height ** 2), 2)

def get_bmi_status(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def calculate_calories_to_burn(current_weight, goal_weight, weeks):
    weight_loss = current_weight - goal_weight
    calories_needed = weight_loss * 7700  # 7700 calories per kg
    weekly_calories = round(calories_needed / weeks, 2)
    return weekly_calories

def bmi_form(request):
    if request.method == 'POST':
        form = BMIForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            bmi = calculate_bmi(data['current_weight'], data['height'])
            bmi_status = get_bmi_status(bmi)
            calories_to_burn = calculate_calories_to_burn(
                data['current_weight'], data['goal_weight'], data['estimated_weeks']
            )
            context = {
                'bmi': bmi,
                'bmi_status': bmi_status,
                'calories_to_burn': calories_to_burn,
                'goal_weight': data['goal_weight'],
                'estimated_weeks': data['estimated_weeks']
            }
            return render(request, 'bmiapp/bmi_result.html', context)
    else:
        form = BMIForm()
    return render(request, 'bmiapp/bmi_form.html', {'form': form})
