from django.db import models

class HighScore(models.Model):
    user = models.CharField(max_length=40)
    score = models.IntegerField(default=-1)
    def __str__(self):
        return self.user + ": " + str(self.score)
