from rest_framework import serializers
from .models import FitnessPlan

class FitnessPlanSerializer(serializers.ModelSerializer):
    trainer_name = serializers.CharField(source='trainer.username', read_only=True)

    class Meta:
        model = FitnessPlan
        fields = '__all__'
        read_only_fields = ['trainer']


class PublicPlanSerializer(serializers.ModelSerializer):
    trainer_name = serializers.CharField(source='trainer.username')

    class Meta:
        model = FitnessPlan
        fields = ['id', 'title', 'trainer_name', 'price']

