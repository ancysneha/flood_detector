import requests
import streamlit as st

def get_weather(city):
    # Get the API key from Streamlit Secrets
    API_KEY = st.secrets["API_KEY"]

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url, timeout=5)
        data = response.json()

        print("Weather API raw response:", data)  # DEBUG

        if data.get("cod") != 200:
            return None

        return {
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "pressure": data["main"]["pressure"],
            "description": data["weather"][0]["description"].title()
        }

    except Exception as e:
        print("Weather API error:", e)
        return None
