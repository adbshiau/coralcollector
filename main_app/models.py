from django.db import models
from django.urls import reverse

TYPE = (
    ('S', 'Soft'),
    ('L', 'Large Polyp Stony'),
    ('P', 'Small Polyp Stony'),
    ('A', 'Anemone')
)

DIFFICULTY = (
    ('V', 'Very Sensitive'),
    ('S', 'Sensitive'),
    ('M', 'Moderate'),
    ('H', 'Hardy'),
    ('A', 'Very Hardy')
)

LIGHTING = (
    ('L', 'Low'),
    ('M', 'Medium'),
    ('H', 'High'),
    ('V', 'Very High')
)

WATER_FLOW = (
    ('L', 'Low'),
    ('M', 'Moderate'),
    ('S', 'Strong')
)

# Create your models here.
class Coral(models.Model):
    trade_name = models.CharField(max_length=100)
    scientific_name = models.CharField(max_length=100)
    coral_type = models.CharField(
        max_length=10,
        choices=TYPE,
        default=TYPE[0][0]
        )
    difficulty = models.CharField(
        max_length=10,
        choices=DIFFICULTY,
        default=DIFFICULTY[2][0]
        )
    lighting = models.CharField(
        max_length=10,
        choices=LIGHTING,
        default=LIGHTING[1][0]
        )
    water_flow = models.CharField(
        max_length=10,
        choices=WATER_FLOW,
        default=WATER_FLOW[1][0]
        )
    notes = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.trade_name} is a/an {self.coral_type}."

    def get_absolute_url(self):
        return reverse('detail', kwargs={'coral_id': self.id})

class Test(models.Model):
    date = models.DateField()
    temp = models.DecimalField(max_digits=5, decimal_places=2)
    kh = models.DecimalField(max_digits=3, decimal_places=1)
    po4 = models.DecimalField(max_digits=3, decimal_places=1)
    no3 = models.IntegerField()

    coral = models.ForeignKey(Coral, on_delete=models.CASCADE)

    def __str__(self):
        return f"Tests done on {self.date}."
