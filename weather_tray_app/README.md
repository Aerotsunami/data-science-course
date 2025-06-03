# Weather Tray App

A simple Python application that displays current weather information in the Windows system tray. It fetches data from the [OpenWeatherMap](https://openweathermap.org/) API and updates periodically.

## Requirements
- Python 3.8+
- `pystray`
- `Pillow`
- `requests`

Install dependencies with:

```bash
pip install -r requirements.txt
```

## Configuration
1. Obtain a free API key from [OpenWeatherMap](https://openweathermap.org/api).
2. Edit `main.py` and set `API_KEY` to your OpenWeatherMap API key.
3. Optionally change the default `CITY` and `UPDATE_INTERVAL` values.

## Running
Execute the script on a Windows machine:

```bash
python main.py
```

The application will show an icon in the system tray with the current temperature and weather description.
