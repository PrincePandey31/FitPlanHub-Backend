from django.urls import path
from .views import DietSuggestionView

urlpatterns = [
    path('diet/suggest/<int:plan_id>/', DietSuggestionView.as_view()),
]
