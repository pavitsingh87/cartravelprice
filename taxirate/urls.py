from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    # Include the app's URLs under the 'distance/' prefix.
    path('distance/', include('distanceapp.urls')),
]
