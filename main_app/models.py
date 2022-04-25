from django.db import models

# Create your models here.
class Coral(models.Model):
    trade_name = models.CharField(max_length=100)
    scientific_name = models.CharField(max_length=100)
    coral_type = models.CharField(max_length=50)
    difficulty = models.CharField(max_length=50)
    lighting = models.CharField(max_length=50)
    water_flow = models.CharField(max_length=50)
    notes = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.trade_name} is a/an {self.coral_type}."

