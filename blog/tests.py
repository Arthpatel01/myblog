# from django.test import TestCase
#
# # Create your tests here.
#
# from cryptography.fernet import Fernet
# import os
#
# # Generate a secure 256-bit key
# key = Fernet.generate_key()
#
# # Generate a 128-bit nonce
# nonce = os.urandom(16)
#
# # Generate a 16-byte salt
# salt = os.urandom(16)
#
# # Create an instance of Fernet cipher
# cipher = Fernet(key)
#
# print('---------------->>nonce', nonce.decode())
# print('---------------->>salt', salt)
# print('---------------->>cipher', cipher)

import requests
from ipware import get_client_ip

def get_user_weather(request):
    # Get the user's location
    client_ip, is_routable = get_client_ip(request)
    if client_ip is None:
        return None

    # Retrieve location data using IP address
    url = f'http://ip-api.com/json/{client_ip}'
    response = requests.get(url)
    if response.status_code != 200:
        return None

    location_data = response.json()
    print('------------->>', location_data)
    lat = location_data['lat']
    lon = location_data['lon']

    # Retrieve weather data using location coordinates
    api_key = 'your_api_key_here'
    url = f'https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true&hourly=temperature_2m,relativehumidity_2m,windspeed_10m&apikey={api_key}'
    response = requests.get(url)
    if response.status_code != 200:
        return None

    weather_data = response.json()['current_weather']
    return weather_data['temperature_2m'], weather_data['relativehumidity_2m'], weather_data['windspeed_10m']
