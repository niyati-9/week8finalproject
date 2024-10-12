# bmiapp/views.py
import pandas as pd
from django.shortcuts import render
from .forms import BMIForm
import os

def calculate_bmi(request):
    bmi = None
    category = None
    data = []  # Store individual input data

    if request.method == 'POST':
        form = BMIForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            height = form.cleaned_data['height']
            weight = form.cleaned_data['weight']

            # Create a DataFrame to perform the BMI calculation using Pandas
            df = pd.DataFrame({'Name': [name], 'Height': [height], 'Weight': [weight]})
            df['BMI'] = df['Weight'] / (df['Height'] ** 2)

            # Categorize the BMI
            conditions = [
                (df['BMI'] < 18.5),
                (df['BMI'] >= 18.5) & (df['BMI'] < 24.9),
                (df['BMI'] >= 25) & (df['BMI'] < 29.9),
                (df['BMI'] >= 30)
            ]
            categories = ['Underweight', 'Normal weight', 'Overweight', 'Obese']
            df['Category'] = pd.cut(df['BMI'], bins=[0, 18.5, 24.9, 29.9, 100], labels=categories, include_lowest=True)

            # Extract calculated values
            bmi = df['BMI'].iloc[0]
            category = df['Category'].iloc[0]
            data = df.to_dict('records')

            # Save the result to a CSV file (optional)
            output_csv_path = 'bmiapp/data/bmi_results.csv'
            if not os.path.exists('bmiapp/data'):
                os.makedirs('bmiapp/data')

            if os.path.exists(output_csv_path):
                df.to_csv(output_csv_path, mode='a', header=False, index=False)  # Append to existing CSV
            else:
                df.to_csv(output_csv_path, index=False)  # Create a new CSV

    else:
        form = BMIForm()

    return render(request, 'bmiapp/bmi_form.html', {
        'form': form,
        'bmi': bmi,
        'category': category,
        'data': data
    })
