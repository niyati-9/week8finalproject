import pandas as pd
import numpy as np
from django.shortcuts import render
from .forms import BMICalculatorForm
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Step 1: Create a sample dataset based on the given table
data = {
    'BMI': [17, 18, 21, 23, 24, 26, 28, 30, 32, 35, 37, 40],  # Example BMI values covering all ranges
    'ActivityLevel': [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4],   # 1=Sedentary, 2=Lightly Active, 3=Moderately Active, 4=Very Active
    'CalorieDeficit': [-500, -400, -300, -300, -400, -500, -600, -700, -700, -800, -800, -900],  # Deficit for weight loss
    'CalorieSurplus': [500, 500, 300, 300, 300, 0, 0, 0, 0, 0, 0, 0]  # Surplus for weight gain, N/A cases are set to 0
}

# Create the DataFrame
df = pd.DataFrame(data)

# Feature matrix and target variables
X = df[['BMI', 'ActivityLevel']]
y_deficit = df['CalorieDeficit']
y_surplus = df['CalorieSurplus']

# Train-test split
X_train, X_test, y_train_deficit, y_test_deficit = train_test_split(X, y_deficit, test_size=0.2, random_state=42)
_, _, y_train_surplus, y_test_surplus = train_test_split(X, y_surplus, test_size=0.2, random_state=42)

# Train the models
model_deficit = LinearRegression()
model_deficit.fit(X_train, y_train_deficit)

model_surplus = LinearRegression()
model_surplus.fit(X_train, y_train_surplus)

# Prediction function
def predict_calories(bmi, activity_level, goal="lose"):
    input_data = np.array([[bmi, activity_level]], dtype=float)
    if goal == "lose":
        return model_deficit.predict(input_data)[0]
    elif goal == "gain":
        return model_surplus.predict(input_data)[0]
    else:
        raise ValueError("Invalid goal. Choose 'lose' or 'gain'.")

# View to handle form input and predict calories
def bmi_calculator(request):
    bmi = None
    activity_level = None
    calorie_deficit = None
    calorie_surplus = None

    if request.method == "POST":
        form = BMICalculatorForm(request.POST)
        if form.is_valid():
            weight = form.cleaned_data['weight']
            height = form.cleaned_data['height']
            activity_level = int(form.cleaned_data['activity_level'])

            # Calculate BMI
            bmi = weight / (height ** 2)

            # Calculate calorie deficit and surplus
            calorie_deficit = predict_calories(bmi, activity_level, goal="lose")
            calorie_surplus = predict_calories(bmi, activity_level, goal="gain")
    
    else:
        form = BMICalculatorForm()

    return render(request, 'bmiapp/bmi_form.html', {
        'form': form,
        'bmi': bmi,
        'activity_level': activity_level,
        'calorie_deficit': calorie_deficit,
        'calorie_surplus': calorie_surplus
    })
