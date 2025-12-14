from django.db import models
from accounts.models import User

class FitnessPlan(models.Model):
    trainer = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    duration = models.IntegerField(help_text="Duration in days")
    created_at = models.DateTimeField(auto_now_add=True)

