from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import DietRecommendation
from plans.models import FitnessPlan
from subscriptions.models import Subscription
from .ai_engine import generate_diet

class DietSuggestionView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, plan_id):
        plan = FitnessPlan.objects.get(id=plan_id)

        # check subscription
        if not Subscription.objects.filter(user=request.user, plan=plan).exists():
            return Response({"error": "Subscribe to plan first"}, status=403)

        ai_result = generate_diet(plan.title, plan.duration)

        diet, created = DietRecommendation.objects.get_or_create(
            user=request.user,
            plan=plan,
            defaults=ai_result
        )

        return Response({
            "message": "AI diet generated",
            "diet": ai_result
        })

