import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise ValueError("API_KEY not found")

BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        return response.json()

    elif response.status_code == 429:
        return {"error": "Too many requests. Try later."}

    else:
        return {"error": f"Error: {response.status_code}"}

# Do NOT log user location data.
# City names are personal data and logging them can violate privacy laws like GDPR.