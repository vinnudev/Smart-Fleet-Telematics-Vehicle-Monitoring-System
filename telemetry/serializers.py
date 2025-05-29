# telemetry/serializers.py
from rest_framework import serializers
from .models import Vehicle, TelemetryData

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['id', 'vin', 'name', 'last_seen']

class TelemetryDataSerializer(serializers.ModelSerializer):
    vin = serializers.CharField(write_only=True)

    class Meta:
        model = TelemetryData
        fields = ['id', 'vehicle', 'vin', 'lat', 'lon', 'speed', 'fuel', 'timestamp']
        read_only_fields = ['vehicle', 'id']

    def validate(self, data):
        vin = data.pop('vin', None)
        if vin:
            vehicle, _ = Vehicle.objects.get_or_create(vin=vin)
            data['vehicle'] = vehicle
        return data
