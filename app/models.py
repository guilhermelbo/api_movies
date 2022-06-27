from django.db import models

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=120)
    genre = models.CharField(max_length=120)
    country = models.CharField(max_length=120)
    directed_by = models.CharField(max_length=120)
    release_date = models.DateField()
    synopsis = models.TextField()