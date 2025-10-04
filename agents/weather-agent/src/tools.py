import requests
from langchain_core.tools import tool
from typing import Dict, Any, Tuple
from src.prompt import WEATHER_TOOL_DESCRIPTION


def get_coordinates(location: str) -> Tuple[float, float, str]:
    """
    Convert location name to latitude and longitude using Open-Meteo Geocoding API.
    """
    geocoding_url = "https://geocoding-api.open-meteo.com/v1/search"
    params = {"name": location, "count": 1, "language": "en", "format": "json"}

    response = requests.get(geocoding_url, params=params)
    response.raise_for_status()

    data = response.json()
    if not data.get("results"):
        raise ValueError(f"Location '{location}' not found")

    result = data["results"][0]
    lat = result["latitude"]
    lon = result["longitude"]
    full_name = f"{result['name']}, {result.get('admin1', '')}, {result['country']}"

    return lat, lon, full_name


def fetch_weather_data(lat: float, lon: float) -> Dict[str, Any]:
    """
    Fetch weather data from Open-Meteo Weather Forecast API.

    This provides:
    - Current weather conditions
    - Hourly forecast for up to 16 days
    - Daily forecast for up to 16 days
    """
    weather_url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "current": [
            "temperature_2m",
            "relative_humidity_2m",
            "apparent_temperature",
            "precipitation",
            "weather_code",
            "cloud_cover",
            "wind_speed_10m",
            "wind_direction_10m",
        ],
        "hourly": [
            "temperature_2m",
            "relative_humidity_2m",
            "precipitation_probability",
            "precipitation",
            "weather_code",
            "cloud_cover",
            "wind_speed_10m",
        ],
        "daily": [
            "weather_code",
            "temperature_2m_max",
            "temperature_2m_min",
            "precipitation_sum",
            "precipitation_probability_max",
            "wind_speed_10m_max",
        ],
        "timezone": "auto",
        "forecast_days": 8,
    }

    response = requests.get(weather_url, params=params)
    response.raise_for_status()

    return response.json()


def get_weather_description(weather_code: int) -> str:
    """
    Convert WMO weather code to human-readable description.
    """
    weather_codes = {
        0: "Clear sky",
        1: "Mainly clear",
        2: "Partly cloudy",
        3: "Overcast",
        45: "Foggy",
        48: "Depositing rime fog",
        51: "Light drizzle",
        53: "Moderate drizzle",
        55: "Dense drizzle",
        56: "Light freezing drizzle",
        57: "Dense freezing drizzle",
        61: "Slight rain",
        63: "Moderate rain",
        65: "Heavy rain",
        66: "Light freezing rain",
        67: "Heavy freezing rain",
        71: "Slight snow fall",
        73: "Moderate snow fall",
        75: "Heavy snow fall",
        77: "Snow grains",
        80: "Slight rain showers",
        81: "Moderate rain showers",
        82: "Violent rain showers",
        85: "Slight snow showers",
        86: "Heavy snow showers",
        95: "Thunderstorm",
        96: "Thunderstorm with slight hail",
        99: "Thunderstorm with heavy hail",
    }
    return weather_codes.get(weather_code, "Unknown")


def format_weather_response(weather_data: Dict[str, Any], location: str) -> str:
    """
    Format the weather data into a human-readable string.
    """
    current = weather_data.get("current", {})
    hourly = weather_data.get("hourly", {})
    daily = weather_data.get("daily", {})

    # Current conditions
    temp = current.get("temperature_2m", "N/A")
    feels_like = current.get("apparent_temperature", "N/A")
    humidity = current.get("relative_humidity_2m", "N/A")
    wind_speed = current.get("wind_speed_10m", "N/A")
    weather_code = current.get("weather_code", 0)
    weather_desc = get_weather_description(weather_code)
    clouds = current.get("cloud_cover", "N/A")
    precipitation = current.get("precipitation", 0)

    result = f"Weather for {location}:\n\n"
    result += "CURRENT CONDITIONS:\n"
    result += f"Temperature: {temp}°C (feels like {feels_like}°C)\n"
    result += f"Conditions: {weather_desc}\n"
    result += f"Humidity: {humidity}%\n"
    result += f"Wind Speed: {wind_speed} km/h\n"
    result += f"Cloud Coverage: {clouds}%\n"
    result += f"Current Precipitation: {precipitation} mm\n\n"

    # Hourly forecast (next 24 hours)
    if hourly and "time" in hourly:
        result += "HOURLY FORECAST (Next 24 hours):\n"
        times = hourly.get("time", [])
        temps = hourly.get("temperature_2m", [])
        precip_prob = hourly.get("precipitation_probability", [])
        precip = hourly.get("precipitation", [])
        codes = hourly.get("weather_code", [])

        for i in range(min(24, len(times))):
            time_str = times[i].split("T")[1] if "T" in times[i] else times[i]
            temp_val = temps[i] if i < len(temps) else "N/A"
            prob_val = precip_prob[i] if i < len(precip_prob) else 0
            precip_val = precip[i] if i < len(precip) else 0
            code_val = codes[i] if i < len(codes) else 0
            desc_val = get_weather_description(code_val)

            result += f"  {time_str}: {temp_val}°C, {desc_val}, "
            result += f"Rain: {prob_val}% ({precip_val}mm)\n"
        result += "\n"

    # Daily forecast (next 7 days)
    if daily and "time" in daily:
        result += "DAILY FORECAST (Next 7 days):\n"
        dates = daily.get("time", [])
        temp_max = daily.get("temperature_2m_max", [])
        temp_min = daily.get("temperature_2m_min", [])
        precip_sum = daily.get("precipitation_sum", [])
        precip_prob = daily.get("precipitation_probability_max", [])
        codes = daily.get("weather_code", [])

        for i in range(min(7, len(dates))):
            date_str = dates[i]
            max_val = temp_max[i] if i < len(temp_max) else "N/A"
            min_val = temp_min[i] if i < len(temp_min) else "N/A"
            precip_val = precip_sum[i] if i < len(precip_sum) else 0
            prob_val = precip_prob[i] if i < len(precip_prob) else 0
            code_val = codes[i] if i < len(codes) else 0
            desc_val = get_weather_description(code_val)

            day_label = "Today" if i == 0 else f"Day +{i}"
            result += f"  {day_label} ({date_str}): {min_val}°C to {max_val}°C, "
            result += f"{desc_val}, Rain: {prob_val}% ({precip_val}mm total)\n"
        result += "\n"

    return result


@tool(
    "weather_tool",
    description=WEATHER_TOOL_DESCRIPTION,
)
def weather_tool(location: str) -> str:
    try:
        # Step 1: Convert location to coordinates
        lat, lon, full_location = get_coordinates(location)
        print(f"Coordinates for {location}: lat={lat}, lon={lon}")
        print(f"Full location: {full_location}")

        # Step 2: Fetch weather data using Open-Meteo API
        weather_data = fetch_weather_data(lat, lon)

        # Step 3: Format and return the response
        formatted_response = format_weather_response(weather_data, full_location)
        print(formatted_response)

        return formatted_response

    except requests.exceptions.HTTPError as e:
        return f"HTTP Error: {str(e)}. Unable to fetch weather data."
    except ValueError as e:
        return f"Error: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"


tools = [weather_tool]
