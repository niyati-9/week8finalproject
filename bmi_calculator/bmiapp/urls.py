from django.urls import path
from .views import bmi_calculator

urlpatterns = [
    path('', bmi_calculator, name='bmi_calculator'),
]
