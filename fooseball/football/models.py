from django.db import models

# Create your models here.
class Score(models.Model):
    name = models.CharField(max_length = 200)
    score1 = models.IntegerField(default=0)
    score2 = models.IntegerField(default=0)

    class Meta:
        def __str__(self):
            return self.name