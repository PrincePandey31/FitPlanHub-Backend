from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Subscription
from plans.models import FitnessPlan

class SubscribeView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, plan_id):
        plan = FitnessPlan.objects.get(id=plan_id)
        Subscription.objects.get_or_create(user=request.user, plan=plan)
        return Response({"message": "Subscribed successfully"})

