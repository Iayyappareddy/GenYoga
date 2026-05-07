from django.db import models
from recommendations.models import YogaPose

class CouresDay(models.Model):
    day = models.IntegerField()
    pose = models.ForeignKey(YogaPose, on_delete=models.CASCADE)
    def __str__(self):
        return f'Day : {self.day} - {self.pose}'