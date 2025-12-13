"""Test night/day weather emoji detection"""

def get_weather_emoji(conditions, time_str=None):
    """Get emoji based on weather conditions and time of day.
    
    Args:
        conditions: Weather condition string
        time_str: Optional ISO format time string (e.g., "2024-12-12T22:00")
                  If provided and it's nighttime, uses night-appropriate emojis
    """
    # Determine if it's nighttime (6 PM to 6 AM)
    is_night = False
    if time_str:
        try:
            from datetime import datetime
            if 'T' in time_str:
                dt = datetime.fromisoformat(time_str.replace('Z', '+00:00'))
                hour = dt.hour
                is_night = hour >= 18 or hour < 6  # 6 PM to 6 AM
        except:
            pass
    
    # Night-specific emojis
    if is_night:
        night_emoji = {
            "Clear sky": "🌙",
            "Mainly clear": "🌙",
            "Partly cloudy": "☁️",
            "Overcast": "☁️",
            "Foggy": "🌫️",
            "Depositing rime fog": "🌫️",
            "Light drizzle": "🌧️",
            "Moderate drizzle": "🌧️",
            "Dense drizzle": "🌧️",
            "Slight rain": "🌧️",
            "Moderate rain": "🌧️",
            "Heavy rain": "⛈️",
            "Slight snow": "🌨️",
            "Moderate snow": "❄️",
            "Heavy snow": "❄️",
            "Snow grains": "❄️",
            "Slight rain showers": "🌧️",
            "Moderate rain showers": "🌧️",
            "Violent rain showers": "⛈️",
            "Slight snow showers": "🌨️",
            "Heavy snow showers": "❄️",
            "Thunderstorm": "⛈️",
            "Thunderstorm with slight hail": "⛈️",
            "Thunderstorm with heavy hail": "⛈️"
        }
        return night_emoji.get(conditions, "🌙")
    
    # Daytime emojis
    weather_emoji = {
        "Clear sky": "☀️",
        "Mainly clear": "🌤️",
        "Partly cloudy": "⛅",
        "Overcast": "☁️",
        "Foggy": "🌫️",
        "Depositing rime fog": "🌫️",
        "Light drizzle": "🌦️",
        "Moderate drizzle": "🌧️",
        "Dense drizzle": "🌧️",
        "Slight rain": "🌧️",
        "Moderate rain": "🌧️",
        "Heavy rain": "⛈️",
        "Slight snow": "🌨️",
        "Moderate snow": "❄️",
        "Heavy snow": "❄️",
        "Snow grains": "❄️",
        "Slight rain showers": "🌦️",
        "Moderate rain showers": "🌧️",
        "Violent rain showers": "⛈️",
        "Slight snow showers": "🌨️",
        "Heavy snow showers": "❄️",
        "Thunderstorm": "⛈️",
        "Thunderstorm with slight hail": "⛈️",
        "Thunderstorm with heavy hail": "⛈️"
    }
    return weather_emoji.get(conditions, "🌤️")


# Test the function
if __name__ == "__main__":
    print("Testing Night/Day Weather Emoji Detection")
    print("=" * 60)
    
    test_cases = [
        ("Clear sky", "2024-12-12T14:00", "Daytime (2 PM)"),
        ("Clear sky", "2024-12-12T22:00", "Nighttime (10 PM)"),
        ("Clear sky", "2024-12-12T03:00", "Nighttime (3 AM)"),
        ("Clear sky", "2024-12-12T08:00", "Daytime (8 AM)"),
        ("Mainly clear", "2024-12-12T19:00", "Nighttime (7 PM)"),
        ("Mainly clear", "2024-12-12T12:00", "Daytime (12 PM)"),
        ("Partly cloudy", "2024-12-12T23:00", "Nighttime (11 PM)"),
        ("Slight rain", "2024-12-12T21:00", "Nighttime (9 PM)"),
        ("Clear sky", None, "No time (default)"),
    ]
    
    for condition, time_str, description in test_cases:
        emoji = get_weather_emoji(condition, time_str)
        print(f"{description:25} | {condition:20} | {emoji}")
    
    print("\n" + "=" * 60)
    print("Expected Results:")
    print("  - Daytime clear sky should show: ☀️")
    print("  - Nighttime clear sky should show: 🌙")
    print("  - Daytime mainly clear should show: 🌤️")
    print("  - Nighttime mainly clear should show: 🌙")
    print("  - No time provided should default to daytime emojis")
