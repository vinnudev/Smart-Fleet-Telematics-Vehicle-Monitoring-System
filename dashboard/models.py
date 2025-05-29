# models.py
from django.db import models

class Telemetry(models.Model):
    vin = models.CharField(max_length=32)
    lat = models.FloatField()
    lon = models.FloatField()
    speed = models.FloatField()
    fuel = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.vin} @ {self.timestamp}"
