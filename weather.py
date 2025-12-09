"""
Weather API Script
Gets current temperature for any location using Open-Meteo API (free, no API key required)
"""

import requests
import sys
from datetime import datetime

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
        # Check if --select or -s flag is present
        interactive = '--select' in sys.argv or '-s' in sys.argv
        
        # Remove flag from arguments and join location
        args = [arg for arg in sys.argv[1:] if arg not in ['--select', '-s']]
        location_arg = ' '.join(args) if args else None
        
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
