import requests
import pandas as pd

# Function to fetch weather data
def fetch_weather_data(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    complete_url = f"{base_url}?q={city}&appid={api_key}&units=metric"
    response = requests.get(complete_url)
    return response.json()

# Example usage
api_key = "Your_API_Key"
city = input("Enter city name: ")
weather_data = fetch_weather_data(city, api_key)
if weather_data:
    print("Weather Information:")
    print(f"Temperature: {weather_data['main']['temp']}°C")
    print(f"Humidity: {weather_data['main']['humidity']}%")
    print(f"Description: {weather_data['weather'][0]['description']}")
else:
    print("City not found.")