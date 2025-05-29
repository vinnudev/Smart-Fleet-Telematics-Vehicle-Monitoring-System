from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.utils.timezone import now

from .models import Vehicle, TelemetryData
from .serializers import TelemetryDataSerializer, VehicleSerializer

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer


class TelemetryViewSet(viewsets.ModelViewSet):
    queryset = TelemetryData.objects.all()
    serializer_class = TelemetryDataSerializer

    @action(detail=False, methods=['post'], url_path='ingest')
    def ingest(self, request):
        vin = request.data.get('vin')
        print("Incoming VIN:", vin)  # 👈 Debug print
        if not vin:
            return Response({'error': 'VIN is required'}, status=400)

        vehicle, _ = Vehicle.objects.get_or_create(vin=vin, defaults={"name": vin})
        vehicle.last_seen = now()
        vehicle.save()

        data = request.data.copy()
        data['vehicle'] = vehicle.id
        print("Final Payload to Serializer:", data)  # 👈 Debug print

        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'ok'}, status=201)

        print("Serializer Errors:", serializer.errors)  # 👈 Debug print
        return Response(serializer.errors, status=400)


