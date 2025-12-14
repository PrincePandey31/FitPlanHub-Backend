from django.db import models
from plans.models import FitnessPlan
from accounts.models import User

class DietRecommendation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plan = models.ForeignKey(FitnessPlan, on_delete=models.CASCADE)

    calories = models.IntegerField()
    protein = models.IntegerField(help_text="grams per day")
    carbs = models.IntegerField(help_text="grams per day")
    fats = models.IntegerField(help_text="grams per day")

    diet_type = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

