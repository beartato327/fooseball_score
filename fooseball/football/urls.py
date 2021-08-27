from django.urls import path
from .views import ScoreListView, ScoreCreateView

urlpatterns = [
    path('scores/', ScoreListView.as_view()),
    path('scores/new_score', ScoreCreateView.as_view(), name='new_score'),
]