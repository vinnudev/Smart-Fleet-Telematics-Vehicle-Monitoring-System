from django.db import models

# Create your models here.
class Vehicle(models.Model):
    vin = models.CharField(max_length=17, unique=True)
    name = models.CharField(max_length=100)
    last_seen = models.DateTimeField(null=True)

    def __str__(self):
        return f"{self.name} ({self.vin})"

class TelemetryData(models.Model): 
    vehicle  = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    speed = models.FloatField()
    fuel_level = models.FloatField()
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return f"{self.vehicle.vin} @ {self.timestamp}"