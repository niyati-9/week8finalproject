from django.shortcuts import render
from .forms import BMIForm

def bmi_calculator(request):
    bmi = None
    if request.method == 'POST':
        form = BMIForm(request.POST)
        if form.is_valid():
            weight = form.cleaned_data['weight']
            height = form.cleaned_data['height']
            bmi = weight / (height ** 2)  # BMI calculation
    else:
        form = BMIForm()

    return render(request, 'bmiapp/bmi_form.html', {'form': form, 'bmi': bmi})
