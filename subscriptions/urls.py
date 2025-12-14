from django.urls import path
from .views import SubscribeView

urlpatterns = [
    path('subscribe/<int:plan_id>/', SubscribeView.as_view(), name='subscribe-plan'),
]
