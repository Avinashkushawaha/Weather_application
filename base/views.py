from django.shortcuts import render
import requests

# Create your views here.
API_KEY = 'https://api.openweathermap.org/data/2.5/weather?q=Bangalore&appid=689c5c1088b7cbe6e1a9458020107bc0'

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?q=Bangalore&appid=689c5c1088b7cbe6e1a9458020107bc0"

def get_weather(city_name):
    """Fetch weather data from the weather API"""
    params = {
        'q': city_name,
        'appid': API_KEY,
        'units': 'metric',  # You can also use 'imperial' for Fahrenheit
    }
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None
    

def weather_view(request):
    """View to display weather data"""
    city = request.GET.get('city', 'Delhi')  # Default city is Delhi
    weather_data = get_weather(city)
    
    context = {
        'weather_data': weather_data,
        'city': city,
    }
    
    return render(request, 'weather.html', context)    