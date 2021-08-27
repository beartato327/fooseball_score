from django.urls import path
from .views import ScoreListView, ScoreCreateView

urlpatterns = [
    path('', ScoreListView.as_view(), name=''),
    path('new_score', ScoreCreateView.as_view(), name='new_score'),
]