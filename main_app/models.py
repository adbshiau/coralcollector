from django.db import models
from django.urls import reverse

# Create your models here.
class Coral(models.Model):
    trade_name = models.CharField(max_length=100)
    scientific_name = models.CharField(max_length=100)
    coral_type = models.CharField(max_length=2)
    difficulty = models.CharField(max_length=2)
    lighting = models.CharField(max_length=1)
    water_flow = models.CharField(max_length=1)
    notes = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.trade_name} is a/an {self.coral_type}."

    def get_absolute_url(self):
        return reverse('detail', kwargs={'coral_id': self.id})

class Tests(models.Model):
    date = models.DateField()
    temp = models.DecimalField(max_digits=5, decimal_places=2)
    kh = models.DecimalField(max_digits=3, decimal_places=1)
    po4 = models.DecimalField(max_digits=3, decimal_places=1)
    no3 = models.IntegerField()
