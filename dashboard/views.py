from django.shortcuts import render
from telemetry.models import Vehicle, TelemetryData
from django.http import JsonResponse

from django.http import HttpResponse
from django.utils.timezone import now


def map_view(request):
    latest_data = {}
    all_data = TelemetryData.objects.select_related("vehicle").order_by('-timestamp')
    for entry in all_data:
        if entry.vehicle_id not in latest_data:
            latest_data[entry.vehicle_id] = {
                "vin": entry.vehicle.vin,
                "lat": entry.latitude,
                "lon": entry.longitude,
                "speed": entry.speed,
                "fuel": entry.fuel_level,
                "timestamp": entry.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            }
    return render(request, 'dashboard/map.html', {"vehicles": list(latest_data.values())})

def vehicle_data_api(request):
    latest_data = {}
    all_data = TelemetryData.objects.select_related("vehicle").order_by('-timestamp')
    for entry in all_data:
        if entry.vehicle_id not in latest_data:
            latest_data[entry.vehicle_id] = {
                "vin": entry.vehicle.vin,
                "lat": entry.latitude,
                "lon": entry.longitude,
                "speed": entry.speed,
                "fuel": entry.fuel_level,
                "timestamp": entry.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            }
    return JsonResponse(list(latest_data.values()), safe=False)

