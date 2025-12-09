"""
Test script for weather alerts feature
"""
import requests
from datetime import datetime

def test_weather_alerts(latitude, longitude, location_name):
    """Test fetching weather alerts for a location."""
    print(f"\n{'='*60}")
    print(f"Testing Weather Alerts for: {location_name}")
    print(f"Coordinates: {latitude}, {longitude}")
    print(f"{'='*60}\n")
    
    try:
        url = f"https://api.weather.gov/alerts/active"
        params = {
            'point': f"{latitude},{longitude}",
            'status': 'actual',
            'message_type': 'alert,update'
        }
        
        headers = {
            'User-Agent': '(Weather App Test, github.com/jxwnpvs2mv-netizen/Weather-App)',
            'Accept': 'application/geo+json'
        }
        
        print("Fetching alerts from NWS API...")
        response = requests.get(url, params=params, headers=headers, timeout=10)
        
        print(f"Response Status: {response.status_code}")
        
        if response.status_code != 200:
            print(f"❌ API Error: Status code {response.status_code}")
            return
        
        data = response.json()
        
        if 'features' in data and len(data['features']) > 0:
            alerts = data['features']
            print(f"\n✅ Found {len(alerts)} active alert(s)!\n")
            
            for i, feature in enumerate(alerts, 1):
                props = feature.get('properties', {})
                
                print(f"Alert #{i}:")
                print(f"  Event: {props.get('event', 'Unknown')}")
                print(f"  Severity: {props.get('severity', 'Unknown')}")
                print(f"  Urgency: {props.get('urgency', 'Unknown')}")
                print(f"  Certainty: {props.get('certainty', 'Unknown')}")
                print(f"  Headline: {props.get('headline', 'N/A')}")
                print(f"  Areas: {props.get('areaDesc', 'N/A')}")
                
                onset = props.get('onset', '')
                if onset:
                    try:
                        onset_dt = datetime.fromisoformat(onset.replace('Z', '+00:00'))
                        print(f"  Effective: {onset_dt.strftime('%b %d, %Y at %I:%M %p')}")
                    except:
                        print(f"  Effective: {onset}")
                
                expires = props.get('expires', '')
                if expires:
                    try:
                        expires_dt = datetime.fromisoformat(expires.replace('Z', '+00:00'))
                        print(f"  Expires: {expires_dt.strftime('%b %d, %Y at %I:%M %p')}")
                    except:
                        print(f"  Expires: {expires}")
                
                print()
        else:
            print("ℹ️  No active alerts for this location.")
            print("This is good news - no severe weather expected! ✅")
        
    except Exception as e:
        print(f"❌ Error: {e}")

# Test locations
print("\n" + "="*60)
print("WEATHER ALERTS TEST SUITE")
print("="*60)

# Test 1: Oklahoma (tornado-prone)
test_weather_alerts(35.2226, -97.4395, "Moore, Oklahoma")

# Test 2: Florida (hurricane zone)
test_weather_alerts(25.7617, -80.1918, "Miami, Florida")

# Test 3: Your location (Ohio)
test_weather_alerts(41.1733, -80.7651, "Niles, Ohio")

# Test 4: California (various weather)
test_weather_alerts(34.0522, -118.2437, "Los Angeles, California")

print("\n" + "="*60)
print("TEST COMPLETE")
print("="*60)
print("\nNote: If no alerts are found, that's normal!")
print("Alerts only appear when severe weather is actively threatening.")
print("\nTo test with active alerts, search for locations currently")
print("experiencing severe weather events (check weather.gov).")
