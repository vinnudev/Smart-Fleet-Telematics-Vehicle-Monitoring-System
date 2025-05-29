# telemetry/urls.py
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import VehicleViewSet, TelemetryViewSet


router = DefaultRouter()
router.register(r'vehicles', VehicleViewSet)
router.register(r'telemetry', TelemetryViewSet, basename='telemetry')

urlpatterns = [
    path('', include(router.urls)),
    path('', include('dashboard.urls')),

]
