from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import FitnessPlan
from .serializers import FitnessPlanSerializer
from .permissions import IsTrainer


class FitnessPlanViewSet(ModelViewSet):
    queryset = FitnessPlan.objects.all()
    serializer_class = FitnessPlanSerializer
    permission_classes = [IsAuthenticated, IsTrainer]

    def get_queryset(self):
        return FitnessPlan.objects.filter(trainer=self.request.user)

    def perform_create(self, serializer):
        serializer.save(trainer=self.request.user)


class FeedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        followed_trainers = request.user.follows.values_list(
            'trainer', flat=True
        )
        plans = FitnessPlan.objects.filter(trainer__in=followed_trainers)
        serializer = FitnessPlanSerializer(plans, many=True)
        return Response(serializer.data)

