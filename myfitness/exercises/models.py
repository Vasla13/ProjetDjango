# exercises/models.py

from django.db import models

class Muscle(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Exercise(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    muscles_worked = models.ManyToManyField(Muscle)

    def __str__(self):
        return self.name

