"""
Weather API Script
Gets current temperature for any location using Open-Meteo API (free, no API key required)
"""

import os
import requests
import sys
from datetime import datetime

try:
    # Lazy import; only used if OPENAI_API_KEY is set
    from openai import OpenAI
except Exception:
    OpenAI = None

def get_location_by_name(location_name, auto_select=True):
    """Get coordinates for a location name using geocoding API."""
    try:
        url = "https://geocoding-api.open-meteo.com/v1/search"
        params = {
            'name': location_name,
            'count': 5,
            'language': 'en',
            'format': 'json'
        }
        
        response = requests.get(url, params=params)
        data = response.json()
        
        if 'results' in data and len(data['results']) > 0:
            results = data['results']
            
            if len(results) > 1 and not auto_select:
                print(f"\n📍 Found {len(results)} locations:")
                for i, r in enumerate(results, 1):
                    print(f"   {i}. {r.get('name')}, {r.get('admin1', '')}, {r.get('country')}")
                
                while True:
                    try:
                        choice = input(f"\nSelect (1-{len(results)}) or press Enter for #1: ").strip()
                        selected_index = 0 if choice == '' else int(choice) - 1
                        if 0 <= selected_index < len(results):
                            break
                        print(f"❌ Please enter a number between 1 and {len(results)}")
                    except ValueError:
                        print("❌ Please enter a valid number")
                
                result = results[selected_index]
                print(f"✅ {result.get('name')}, {result.get('admin1', '')}")
            else:
                result = results[0]
            
            return {
                'latitude': result.get('latitude'),
                'longitude': result.get('longitude'),
                'city': result.get('name'),
                'region': result.get('admin1', ''),
                'country': result.get('country')
            }
        
        # If not found, try just the first part (city name)
        if ',' in location_name or ' ' in location_name:
            city_only = location_name.split(',')[0].strip() if ',' in location_name else location_name.split()[0].strip()
            print(f"⚠️ '{location_name}' not found, trying just '{city_only}'...")
            
            params['name'] = city_only
            response = requests.get(url, params=params)
            data = response.json()
            
            if 'results' in data and len(data['results']) > 0:
                results = data['results']
                print(f"\n📍 Found {len(results)} possible locations for '{city_only}':")
                for i, r in enumerate(results[:3], 1):
                    print(f"   {i}. {r.get('name')}, {r.get('admin1', '')}, {r.get('country')}")
                print(f"\n✅ Using: {results[0].get('name')}, {results[0].get('admin1', '')}, {results[0].get('country')}")
                
                result = results[0]
                return {
                    'latitude': result.get('latitude'),
                    'longitude': result.get('longitude'),
                    'city': result.get('name'),
                    'region': result.get('admin1', ''),
                    'country': result.get('country')
                }
        
        print(f"❌ Location '{location_name}' not found")
        print("💡 Try: 'City' or 'City, Country' (e.g., 'Boston' or 'Boston, USA')")
        return None
    except Exception as e:
        print(f"❌ Error searching for location: {e}")
        return None

def get_current_location():
    """Get approximate location based on IP address."""
    try:
        response = requests.get('https://ipapi.co/json/', timeout=5)
        data = response.json()
        
        if data.get('latitude') and data.get('longitude'):
            return {
                'latitude': data.get('latitude'),
                'longitude': data.get('longitude'),
                'city': data.get('city', 'Unknown'),
                'region': data.get('region', 'Unknown'),
                'country': data.get('country_name', 'Unknown')
            }
        
        print("⚠️ Could not determine location from IP")
        return None
    except Exception as e:
        print(f"❌ Error getting location: {e}")
        return None

def get_weather(latitude, longitude):
    """Get current weather data from Open-Meteo API."""
    try:
        url = "https://api.open-meteo.com/v1/forecast"
        params = {
            'latitude': latitude,
            'longitude': longitude,
            'current': 'temperature_2m,relative_humidity_2m,wind_speed_10m,weather_code',
            'temperature_unit': 'fahrenheit',
            'wind_speed_unit': 'mph'
        }
        
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"❌ Error getting weather: {e}")
        return None

def get_weather_description(weather_code):
    """Convert weather code to description."""
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
        61: "Slight rain",
        63: "Moderate rain",
        65: "Heavy rain",
        71: "Slight snow",
        73: "Moderate snow",
        75: "Heavy snow",
        77: "Snow grains",
        80: "Slight rain showers",
        81: "Moderate rain showers",
        82: "Violent rain showers",
        85: "Slight snow showers",
        86: "Heavy snow showers",
        95: "Thunderstorm",
        96: "Thunderstorm with slight hail",
        99: "Thunderstorm with heavy hail"
    }
    return weather_codes.get(weather_code, "Unknown")

def _build_local_overview(location, weather_data, style: str = "concise") -> str:
    """Create a simple local overview without AI (used on quota errors)."""
    current = weather_data.get('current', {}) if weather_data else {}
    temperature = current.get('temperature_2m')
    humidity = current.get('relative_humidity_2m')
    wind = current.get('wind_speed_10m')
    code = current.get('weather_code')
    conditions = get_weather_description(code)
    city = (location or {}).get('city', 'Unknown')
    region = (location or {}).get('region', '')
    country = (location or {}).get('country', '')
    tone_prefix = "Brief:" if style == "concise" else style.capitalize() + ":"
    return (
        f"{tone_prefix} {city}, {region}, {country}: {conditions}. "
        f"Temp {temperature}°F, humidity {humidity}%, wind {wind} mph."
    )

def generate_ai_overview(location, weather_data, model: str = "gpt-4o-mini", style: str = "concise"):
    """Generate an AI-powered weather overview using OpenAI.

    Reads OPENAI_API_KEY from environment. Requires `openai` package.
    Returns a string with the overview, or None if unavailable.
    """
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key or OpenAI is None:
        return None

    try:
        client = OpenAI(api_key=api_key)

        # Build a compact context from available data
        current = weather_data.get('current', {}) if weather_data else {}
        temperature = current.get('temperature_2m')
        humidity = current.get('relative_humidity_2m')
        wind = current.get('wind_speed_10m')
        code = current.get('weather_code')
        conditions = get_weather_description(code)

        city = location.get('city') if location else 'Unknown'
        region = location.get('region') if location else ''
        country = location.get('country') if location else ''

        tone = "concise, friendly" if style == "concise" else style
        prompt = (
            f"Provide a {tone} weather overview for {city}, {region}, {country}. "
            f"Current conditions: {conditions}, temp {temperature}°F, humidity {humidity}%, wind {wind} mph. "
            "Avoid speculation beyond available current data; do not fabricate forecasts. "
            "Keep it short (1-2 sentences)."
        )

        completion = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful weather assistant."},
                {"role": "user", "content": prompt},
            ],
            temperature=0.2,
            max_tokens=120,
        )
        return completion.choices[0].message.content.strip()
    except Exception as e:
        # If quota exceeded or 429, return local summary instead of error text
        msg = str(e).lower()
        if 'insufficient_quota' in msg or 'code: 429' in msg or 'status code: 429' in msg:
            return _build_local_overview(location, weather_data, style=style)
        # Generic fallback keeps things graceful
        return f"(AI overview error: {e})"

def _parse_cli_flags(argv: list[str]):
    """Parse CLI flags and return a dict and remaining args for location.

    Supports:
      --select / -s : interactive selection mode
      --ai          : enable AI overview
      --model NAME  : choose OpenAI model (default gpt-4o-mini)
      --style NAME  : overview style (default concise)
    """
    flags = {"interactive": ('--select' in argv or '-s' in argv), "ai": ('--ai' in argv), "model": "gpt-4o-mini", "style": "concise"}
    remaining = []
    skip_next = False
    for i, arg in enumerate(argv):
        if skip_next:
            skip_next = False
            continue
        if arg in ('--select', '-s', '--ai'):
            continue
        if arg.startswith('--model='):
            flags['model'] = arg.split('=', 1)[1]
            continue
        if arg == '--model' and i + 1 < len(argv):
            flags['model'] = argv[i + 1]
            skip_next = True
            continue
        if arg.startswith('--style='):
            flags['style'] = arg.split('=', 1)[1]
            continue
        if arg == '--style' and i + 1 < len(argv):
            flags['style'] = argv[i + 1]
            skip_next = True
            continue
        # non-flag
        remaining.append(arg)
    return flags, remaining

def main(custom_location=None, interactive=False):
    """Main function to get and display weather."""
    location = get_location_by_name(custom_location, auto_select=not interactive) if custom_location else get_current_location()
    
    if not location:
        print("❌ Could not determine location")
        return
    
    print(f"📍 {location['city']}, {location['region']}, {location['country']}")
    
    weather_data = get_weather(location['latitude'], location['longitude'])
    
    if not weather_data:
        print("❌ Could not fetch weather data")
        return
    
    # Extract current weather
    current = weather_data.get('current', {})
    temperature = current.get('temperature_2m')
    humidity = current.get('relative_humidity_2m')
    wind_speed = current.get('wind_speed_10m')
    weather_code = current.get('weather_code')
    conditions = get_weather_description(weather_code)
    
    # Display results
    print(f"🌡️  {temperature}°F | 💧 {humidity}% | 💨 {wind_speed} mph | {conditions}")

    # Optionally generate AI overview if requested via CLI flag
    # Optionally generate AI overview if requested via CLI flags
    flags, _ = _parse_cli_flags(sys.argv[1:])
    if flags.get('ai'):
        overview = generate_ai_overview(location, weather_data, model=flags.get('model', 'gpt-4o-mini'), style=flags.get('style', 'concise'))
        if overview:
            print("\n🤖 AI Weather Overview:\n" + overview)
        else:
            print("\n🤖 AI Weather Overview unavailable (missing API key or client).")
    
    return temperature

def interactive_mode():
    """Interactive mode to input city and state."""
    print("=" * 50)
    print("🌤️  WEATHER LOOKUP")
    print("=" * 50)
    print("\nOptions:")
    print("  1. Use current location (auto-detect)")
    print("  2. Enter city and state")
    print("  3. Enter any location")
    
    while True:
        choice = input("\nSelect option (1-3): ").strip()
        
        if choice == '1':
            return None
        elif choice == '2':
            city = input("\nEnter city: ").strip()
            state = input("Enter state: ").strip()
            if city and state:
                return f"{city}, {state}"
            if city:
                print(f"⚠️ Using just city: {city}")
                return city
            print("⚠️ No input provided, using current location")
            return None
        elif choice == '3':
            location = input("\nEnter location: ").strip()
            return location if location else None
        
        print("❌ Invalid choice. Please enter 1, 2, or 3")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        flags, remaining = _parse_cli_flags(sys.argv[1:])
        interactive = flags['interactive']
        location_arg = ' '.join(remaining) if remaining else None
        
        if location_arg:
            main(custom_location=location_arg, interactive=interactive)
        else:
            # Just the flag, go to interactive mode
            custom_location = interactive_mode()
            main(custom_location=custom_location, interactive=True)
    else:
        # Interactive mode - prompt user for input
        custom_location = interactive_mode()
        main(custom_location=custom_location, interactive=True)
