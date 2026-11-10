import requests

def weather(city="Patna"):
    try:
        # Get coordinates for the city
        geocode_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1&language=en&format=json"
        geo_response = requests.get(geocode_url, timeout=5).json()

        if not geo_response.get("results"):
            return f"I couldn't find the city {city}."

        lat = geo_response["results"][0]["latitude"]
        lon = geo_response["results"][0]["longitude"]
        city_name = geo_response["results"][0]["name"]

        # Get the weather using coordinates
        weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,wind_speed_10m&timezone=auto"
        weather_data = requests.get(weather_url, timeout=5).json()

        temp = weather_data["current"]["temperature_2m"]
        units_temp = weather_data["current_units"]["temperature_2m"]

        return f"The current temperature in {city_name} is {temp}{units_temp}."
    
    except Exception:
        return "Sorry, I am unable to fetch the weather right now."