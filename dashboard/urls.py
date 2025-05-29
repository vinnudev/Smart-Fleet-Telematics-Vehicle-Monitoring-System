from django.urls import path
from .views import map_view, vehicle_data_api

urlpatterns = [
    path('map/', map_view, name='fleet-map'),
    path('api/latest/', vehicle_data_api, name='vehicle-data-api'),
    
]
