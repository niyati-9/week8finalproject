
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

def calculate_weekly_calories(current_weight, goal_weight, weeks):
    weight_change = abs(current_weight - goal_weight)
    calories_needed = weight_change * 7700  # 7700 calories per kg
    weekly_calories = round(calories_needed / weeks, 2)
    return weekly_calories

def bmi_form(request):
    if request.method == 'POST':
        form = BMIForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            bmi = calculate_bmi(data['current_weight'], data['height'])
            bmi_status = get_bmi_status(bmi)

            current_weight = data['current_weight']
            goal_weight = data['goal_weight']
            estimated_weeks = data['estimated_weeks']

            weekly_calories = calculate_weekly_calories(
                current_weight, goal_weight, estimated_weeks
            )

            # Determine whether user needs to gain or lose weight
            if goal_weight > current_weight:
                action = "gain"
                message = f"You need to gain {goal_weight - current_weight} kg to reach your goal."
            else:
                action = "lose"
                message = f"You need to lose {current_weight - goal_weight} kg to reach your goal."

            context = {
                'bmi': bmi,
                'bmi_status': bmi_status,
                'weekly_calories': weekly_calories,
                'goal_weight': goal_weight,
                'estimated_weeks': estimated_weeks,
                'action': action,
                'message': message,
            }
            return render(request, 'bmiapp/bmi_result.html', context)
    else:
        form = BMIForm()
    return render(request, 'bmiapp/bmi_form.html', {'form': form})
