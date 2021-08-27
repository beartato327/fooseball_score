from django.views.generic import ListView, CreateView
from .models import Score

# Create your views here.
class ScoreListView(ListView):
    queryset = Score.objects.all()
    model = Score
    #template_name = 'football/index.html'

class ScoreCreateView(CreateView):
    model = Score
    fields = ['name', 'score1','score2']
    success_url = '/football/scores'