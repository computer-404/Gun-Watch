import folium
import pandas as pd
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse

def hotspot_map(request):
    # Load state coordinates (assuming a file state_coordinates.csv with 'state', 'latitude', and 'longitude' columns)
    state_coordinates = pd.read_csv('model_app/state_coordinates.csv', delimiter='\t')

    # Load the dataset with state-wise sentiment data
    data = pd.read_csv('model_app/data.csv')

    # Create a map centered on the US
    m = folium.Map(location=[37, -102], zoom_start=4)

    # Add markers for each state based on the 'amount' column
    for index, row in data.iterrows():
        state = row['location']
        count = row['amount']
        latitude, longitude = state_coordinates[state_coordinates['state'] == state][['latitude', 'longitude']].values[0]

        # Create a marker with a tooltip showing the count
        folium.CircleMarker(
            location=[latitude, longitude],
            radius=count * 0.1,  # Adjust the size based on the 'amount' column
            popup=f'State: {state}<br>Count: {count}',
            fill=True,
            fill_color='red',
        ).add_to(m)

    # Save the map as an HTML file
    map_html = m._repr_html_()

    # Create a variable with the URL of the home page
    home_page_url = reverse('home')

    # Return an HTTP response with the HTML content and the home page URL
    return render(request, 'model_app/hotspot_map_content.html', {'home_page_url': home_page_url, 'map_html': map_html})


def home(request):
    return render(request, 'model_app/home.html')

def about_me(request):
    return render(request, 'model_app/about_me.html')

def research(request):
    return render(request, 'model_app/research.html')
