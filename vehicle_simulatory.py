import requests
import random
import time

# ✅ Fixed VINs for 5 vehicles
VINS = ["FLEET001", "FLEET002", "FLEET003", "FLEET004", "FLEET005"]

# ✅ Track positions per VIN
positions = {
    vin: {
        "lat": round(random.uniform(12.9, 13.1), 6),
        "lon": round(random.uniform(77.5, 77.7), 6),
    } for vin in VINS
}

def simulate_movement(vin):
    pos = positions[vin]
    # Simulate small random movement (jitter)
    pos["lat"] += round(random.uniform(-0.001, 0.001), 6)
    pos["lon"] += round(random.uniform(-0.001, 0.001), 6)
    # Keep within bounds
    pos["lat"] = max(12.8, min(13.2, pos["lat"]))
    pos["lon"] = max(77.4, min(77.8, pos["lon"]))
    return pos

while True:
    for vin in VINS:
        pos = simulate_movement(vin)

        payload = {
            "vin": vin,
            "latitude": pos["lat"],
            "longitude": pos["lon"],
            "speed": random.randint(0, 120),
            "fuel_level": random.randint(10, 100),
        }

        try:
            res = requests.post("http://127.0.0.1:8000/api/telemetry/ingest/", json=payload)
            print(f"Sent for {vin}: {payload} | Status: {res.status_code}")
        except Exception as e:
            print(f"Error sending data: {e}")

        time.sleep(1)

    # Optionally wait a bit between full loops
    time.sleep(1)
