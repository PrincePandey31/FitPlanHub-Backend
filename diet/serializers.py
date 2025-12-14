from rest_framework import serializers
from .models import DietRecommendation

class DietSerializer(serializers.ModelSerializer):
    class Meta:
        model = DietRecommendation
        fields = '__all__'
