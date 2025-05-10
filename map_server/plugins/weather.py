def get_weather(city):
    fake_data = {
        "seattle": {"temp": "15°C", "condition": "Cloudy"},
        "new york": {"temp": "20°C", "condition": "Sunny"},
    }
    return fake_data.get(city.lower(), {"error": "City not found"})
