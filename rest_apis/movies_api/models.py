from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Moviedata(models.Model):
    title = models.CharField(max_length=200)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    duration = models.FloatField()


    def __str__(self):
        return self.title