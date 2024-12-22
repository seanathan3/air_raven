from django.db import models

# Create your models here.

class Flight(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    price = models.DecimalField(decimal_places=2, max_digits=7)
    flight_number = models.CharField(max_length=20)
    carrier = models.CharField(max_length=50)

    def __str__(self):
        return self.flight_number


