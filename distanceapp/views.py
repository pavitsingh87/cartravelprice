from django.shortcuts import render
from django.http import JsonResponse
import googlemaps
from django.conf import settings  # Assume you have your API keys in settings
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

def calculate_distance(request):
    if request.method == 'POST':
        origin = request.POST.get('origin')
        destination = request.POST.get('destination')
        
        # Initialize Google Maps client with your API key
        gmaps = googlemaps.Client(key=settings.GOOGLE_MAPS_API_KEY)

        # Use Google Distance Matrix API to find the distance
        distance_result = gmaps.distance_matrix(origin, destination, mode="driving")
        distance = distance_result['rows'][0]['elements'][0]['distance']['value'] / 1000  # distance in km
        distance_text = distance_result['rows'][0]['elements'][0]['distance']['text']
        duration = distance_result['rows'][0]['elements'][0]['duration']['text']

        # Calculate price
        price = 12 if distance <= 12 else 12 + (distance - 1) * 2.5
        price = 0.7 * price  # 3 for the first 5km, and 1 for each additional km
        
        # Construct a URL for the static map with markers for the origin and destination
        static_map_url = f"https://maps.googleapis.com/maps/api/staticmap?size=600x300&path=color:0xff0000ff|weight:5|{origin}|{destination}&markers=color:green|label:O|{origin}&markers=color:red|label:D|{destination}&key={settings.GOOGLE_MAPS_API_KEY}"

        # Return the distance, duration, price, and static map URL as a JSON response
        return JsonResponse({
            'distance': distance_text,
            'duration': duration,
            'price': f"{price:.2f}",
            'map_url': static_map_url
        })

    return render(request, 'index.html')
