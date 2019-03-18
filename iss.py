import requests
import json
from datetime import datetime

def get_iss_location():
    endpoint = 'http://api.open-notify.org/iss-now.json'

    response = requests.get(endpoint)

    return response.json()

def get_iss_pass_time(lat, lon):
    endpoint = 'http://api.open-notify.org/iss-pass.json'
    coordinates = {
        'lat': lat,
        'lon': lon
    }

    response = requests.get(endpoint, params=coordinates)
    date_list = response.json().get('response')
    pass_time_unix = int(date_list[0].get('risetime'))
    
    return datetime.utcfromtimestamp(pass_time_unix).strftime('%Y-%m-%d %H:%M:%S')

def get_iss_pass_time_from_postcode(postcode):
    endpoint = f'http://api.postcodes.io/postcodes/{postcode}'

    response = requests.get(endpoint).json()
    lat = response.get('result').get('latitude')
    lon = response.get('result').get('longitude')

    return get_iss_pass_time(lat, lon)
