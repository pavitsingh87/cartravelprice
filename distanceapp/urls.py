from django.urls import path
from .views import calculate_distance

urlpatterns = [
    path('calculate_distance', calculate_distance, name='calculate_distance'),
    # If you want the URL to be just 'distance/', then change it to path('', calculate_distance, name='calculate_distance'),
]
