from django.urls import path
from . import views

urlpatterns = [
    path('', views.bmi_calculator, name='home'),  # This makes the home page load the BMI calculator form
    path('bmi/', views.bmi_calculator, name='bmi_calculator'),
]
