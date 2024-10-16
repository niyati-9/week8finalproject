from django.db import models

class BMICalculation(models.Model):
    weight = models.FloatField()
    height = models.FloatField()
    bmi = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"BMI: {self.bmi} (Weight: {self.weight}, Height: {self.height})"
