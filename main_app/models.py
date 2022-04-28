from django.db import models
from django.urls import reverse

TYPE = (
    ('S', 'Soft'),
    ('L', 'Large Polyp Stony (LPS)'),
    ('P', 'Small Polyp Stony (SPS)'),
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
class Location(models.Model):
    country = models.CharField(max_length=20)

    def __str__(self):
        return self.country
    
    def get_absolute_url(self):
        return reverse('locations_detail', kwargs={'pk': self.id})

class Coral(models.Model):
    trade_name = models.CharField(max_length=100)
    scientific_name = models.CharField(max_length=100)
    coral_type = models.CharField(
        max_length=1,
        choices=TYPE,
        default=TYPE[0][0]
        )
    difficulty = models.CharField(
        max_length=1,
        choices=DIFFICULTY,
        default=DIFFICULTY[2][0]
        )
    lighting = models.CharField(
        max_length=1,
        choices=LIGHTING,
        default=LIGHTING[1][0]
        )
    water_flow = models.CharField(
        max_length=1,
        choices=WATER_FLOW,
        default=WATER_FLOW[1][0]
        )
    locations = models.ManyToManyField(Location)

    def __str__(self):
        return self.trade_name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'coral_id': self.id})

class Note(models.Model):
    date = models.DateField()
    entry = models.CharField(max_length=250)

    coral = models.ForeignKey(Coral, on_delete=models.CASCADE)

    def __str__(self):
        return f"Added on {self.date}."
    
class Photo(models.Model):
    url = models.CharField(max_length=200)
    cat = models.ForeignKey(Coral, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for cat_id: {self.coral_id} @{self.url}"
