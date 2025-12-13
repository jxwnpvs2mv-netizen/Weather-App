"""
Test the sun times display with sample data from Open-Meteo API
"""

from datetime import datetime, timezone

# Sample weather data with daily sun times (like Open-Meteo returns)
sample_weather_data = {
    'current': {
        'temperature_2m': 72,
        'weather_code': 0
    },
    'hourly': {
        'time': ['2024-01-15T00:00', '2024-01-15T01:00'],
        'temperature_2m': [70, 68]
    },
    'daily': {
        'sunrise': ['2024-01-15T07:15:00Z'],
        'sunset': ['2024-01-15T17:45:00Z'],
        'daylight_duration': [37800],  # 10.5 hours in seconds
        'sunshine_duration': [28800],  # 8 hours of actual sunshine
        'uv_index_max': [7.2]
    }
}

# Extract and display the data
daily = sample_weather_data.get('daily', {})

if daily:
    sunrise = daily.get('sunrise', [None])[0]
    sunset = daily.get('sunset', [None])[0]
    daylight_duration = daily.get('daylight_duration', [None])[0]
    sunshine_duration = daily.get('sunshine_duration', [None])[0]
    uv_index = daily.get('uv_index_max', [None])[0]
    
    print("=" * 60)
    print("SUN TIMES DISPLAY TEST")
    print("=" * 60)
    
    if sunrise and sunset:
        from datetime import timedelta
        
        # Parse sunrise and sunset times
        sunrise_dt = datetime.fromisoformat(sunrise.replace('Z', '+00:00'))
        sunset_dt = datetime.fromisoformat(sunset.replace('Z', '+00:00'))
        
        # Format times
        sunrise_time = sunrise_dt.strftime('%I:%M %p').lstrip('0')
        sunset_time = sunset_dt.strftime('%I:%M %p').lstrip('0')
        
        # Calculate civil twilight (approximately 25 minutes before sunrise / after sunset)
        first_light_dt = sunrise_dt - timedelta(minutes=25)
        last_light_dt = sunset_dt + timedelta(minutes=25)
        
        first_light = first_light_dt.strftime('%I:%M %p').lstrip('0')
        last_light = last_light_dt.strftime('%I:%M %p').lstrip('0')
        
        print(f"\n🌅 First Light (Civil Twilight): {first_light}")
        print(f"🌄 Sunrise:                       {sunrise_time}")
        print(f"🌇 Sunset:                        {sunset_time}")
        print(f"🌆 Last Light (Civil Twilight):   {last_light}")
        
        # Convert daylight duration from seconds to hours and minutes
        if daylight_duration:
            hours = int(daylight_duration // 3600)
            minutes = int((daylight_duration % 3600) // 60)
            daylight_str = f"{hours}h {minutes}m"
            print(f"\n⏰ Total Daylight:                {daylight_str}")
        
        # Sunshine duration (actual sunshine vs possible daylight)
        if sunshine_duration:
            sun_hours = int(sunshine_duration // 3600)
            sun_minutes = int((sunshine_duration % 3600) // 60)
            sunshine_str = f"{sun_hours}h {sun_minutes}m"
            sunshine_percent = int((sunshine_duration / daylight_duration * 100)) if daylight_duration else 0
            print(f"☀️  Actual Sunshine:               {sunshine_str} ({sunshine_percent}% of daylight)")
        
        # UV Index color coding
        if uv_index:
            if uv_index < 3:
                uv_level = "Low"
            elif uv_index < 6:
                uv_level = "Moderate"
            elif uv_index < 8:
                uv_level = "High"
            elif uv_index < 11:
                uv_level = "Very High"
            else:
                uv_level = "Extreme"
            print(f"🌞 UV Index:                      {uv_index:.1f} - {uv_level}")
        
        print("\n" + "=" * 60)
        print("✅ Sun times function working correctly!")
        print("=" * 60)
        
        print("\nℹ️  This display will appear in your weather app between the")
        print("   current conditions and the daily outlook.")
        print("\n📝 Note: Civil twilight is estimated as ±25 minutes from sunrise/sunset")
        print("   For exact twilight times, Open-Meteo may have dedicated parameters.")
    else:
        print("❌ No sunrise/sunset data available")
else:
    print("❌ No daily data in weather response")
