import requests
import requests.exceptions
import os

from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('WEATHER_API_KEY') #api key

# Function to get weather data from OpenWeatherMap API
def get_weather(city):
    
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"


    response = requests.get(url)
    data = response.json()

    if data['cod'] == 200:
        main = data['main']
        temp = main['temp'] - 273.15 # Convert from Kelvin to Celsius

        return f"The temperature in {city} is {temp:.2f}°C."
    else:
        return "Sorry, I couldn't find the weather for that location."