from django.shortcuts import render


# Función para convertir dirección a coordenadas usando Google Maps API
def get_coordinates(address):
    url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {"address": address, "key": "TU_API_KEY"}
    response = requests.get(url, params=params)
    data = response.json()
    if data['status'] == 'OK':
        location = data['results'][0]['geometry']['location']
        return location['lat'], location['lng']
    else:
        return None, None


# Función para obtener datos de clima usando una API de clima
def get_climate_data(lat, lng):
    # Aquí puedes usar una API de clima como OpenWeatherMap
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"lat": lat, "lon": lng, "appid": "TU_API_KEY"}
    response = requests.get(url, params=params)
    data = response.json()
    return data


# Función para obtener datos de producción de café
def get_coffee_production_data(lat, lng):
    # Aquí puedes usar una API de datos agrícolas como USDA o FAO
    url = "https://api.agriculturedata.org/production"
    params = {"lat": lat, "lng": lng}
    response = requests.get(url, params=params)
    data = response.json()
    return data
import requests
import pandas as pd
from django.shortcuts import render


# Ejemplo de uso
def trazado(request):
    address = "Calle Principal, Ciudad, País"
    coordinates = get_coordinates(address)
    if coordinates[0] is not None:
        climate_data = get_climate_data(coordinates[0], coordinates[1])
        coffee_data = get_coffee_production_data(coordinates[0], coordinates[1])
        
        # Crear un DataFrame con los datos
        df = pd.DataFrame({
            "Latitud": [coordinates[0]],
            "Longitud": [coordinates[1]],
            "Temperatura": [climate_data['main']['temp']],
            "Precipitación": [climate_data['weather'][0]['description']],
            "Producción de Café": [coffee_data['production']]
        })
        print(df)
    else:
        print("No se encontraron coordenadas para la dirección proporcionada.")

    context = {"title":"Seguimiento"}
    return render(request, "trazado/trazado.html", context)