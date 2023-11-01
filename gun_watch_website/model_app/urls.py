from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),  # For the "home" view
    path('hotspot_map', views.hotspot_map, name='hotspot_map'),  # For the "hotspot_map" view
    path('about_me', views.about_me, name='about_me'),  # URL pattern for the About Me page
    path('research', views.research, name='research'),  # URL pattern for the Research page

    # Other app-specific URL patterns can be added here
]
