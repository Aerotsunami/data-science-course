# Weather Tray App
# This script fetches weather information from OpenWeatherMap API
# and displays it in the Windows system tray using pystray.

import json
import threading
import time
from datetime import datetime
from pathlib import Path

import requests
from PIL import Image
import pystray


# Replace with your OpenWeatherMap API key
API_KEY = "YOUR_API_KEY"
# City for which to fetch the weather
CITY = "London"
# Update interval in seconds
UPDATE_INTERVAL = 60 * 30  # 30 minutes


class WeatherTrayApp:
    def __init__(self, city: str, api_key: str):
        self.city = city
        self.api_key = api_key
        self.icon = pystray.Icon("weather_tray")
        # Use a blank 1x1 image; icon updates will set the menu title
        self.icon.icon = Image.new("RGB", (1, 1), color=(255, 255, 255))
        self.icon.title = "Weather Tray App"
        self.thread = threading.Thread(target=self.update_loop, daemon=True)

    def fetch_weather(self) -> str:
        url = (
            "https://api.openweathermap.org/data/2.5/weather"
            f"?q={self.city}&appid={self.api_key}&units=metric"
        )
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        temp = data["main"]["temp"]
        description = data["weather"][0]["description"].capitalize()
        return f"{temp:.1f}°C, {description}"

    def update_tooltip(self):
        try:
            weather = self.fetch_weather()
            tooltip = f"{self.city}: {weather} (Updated {datetime.now().strftime('%H:%M')})"
        except Exception as exc:
            tooltip = f"Error fetching weather: {exc}"
        self.icon.title = tooltip

    def update_loop(self):
        while True:
            self.update_tooltip()
            time.sleep(UPDATE_INTERVAL)

    def run(self):
        self.update_tooltip()
        self.thread.start()
        self.icon.run()


if __name__ == "__main__":
    app = WeatherTrayApp(CITY, API_KEY)
    app.run()
