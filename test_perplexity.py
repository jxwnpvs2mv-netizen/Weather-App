"""Test Perplexity AI integration for weather forecasts"""
import requests
from typing import Dict, Any, List

def generate_ai_overview(location: Dict[str, Any], hourly_slice: List[Dict[str, Any]]) -> str:
    """Use Perplexity AI to produce a web-based, human-friendly weather overview from hourly forecast data."""
    # Perplexity API configuration
    perplexity_api_key = "pplx-" + "3TYsMG8TpbstdLN5Zq1ZFobvEMt67FDnM14YYsTrzCLVqjI7"
    
    if not perplexity_api_key:
        return "🌐 Web-Based AI Weather Overview unavailable: API key not configured."

    city = location.get('city', 'Unknown')
    region = location.get('region', '')
    country = location.get('country', '')
    
    # Get current date for context
    from datetime import datetime
    today = datetime.now().strftime('%B %d, %Y')

    # Build hourly data summary for the prompt
    if not hourly_slice:
        return "AI overview unavailable: missing hourly data."
    
    # Format hourly data into readable text (next 48 hours)
    hours_text = []
    for h in hourly_slice[:48]:
        time_str = h.get('time', '')
        temp = h.get('temp_f')
        precip_prob = h.get('precip_prob', 0)
        precip_mm = h.get('precip_mm', 0)
        
        # Format: "2023-12-13T14:00 -> 72°F, 30% precip chance, 0.5mm"
        temp_str = f"{int(temp)}°F" if temp else "N/A"
        hours_text.append(f"{time_str} -> {temp_str}, {precip_prob}% precip, {precip_mm}mm")
    
    hours_blob = "\n".join(hours_text)

    system_msg = (
        "You are a precise, thorough weather forecaster with access to real-time web information. "
        "You will receive hourly weather data and transform it into a richly detailed, practical 2-day forecast "
        "enriched with current web-based weather intelligence from trusted meteorological sources. "
        "Use a natural, flowing narrative style with complete sentences and professional weather language. "
        "Be explicit about when precipitation starts, peaks, and ends with specific time callouts. "
        "Leverage your web search capabilities to provide context about current weather patterns, systems, and trends."
    )

    user_msg = (
        f"Location: {city}, {region}, {country}\n"
        f"Date: {today}\n\n"
        f"HOURLY FORECAST DATA (next 48 hours):\n{hours_blob}\n\n"
        f"Using your web search capabilities, find current weather patterns, advisories, and meteorological context for {city}, {region}. "
        f"Then create a comprehensive forecast for the next 2 days with specific hourly details."
    )

    try:
        # Use Perplexity AI with web search to generate narrative forecast from hourly data
        headers = {
            "Authorization": f"Bearer {perplexity_api_key}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "model": "sonar-pro",  # Perplexity's web-search enabled model
            "messages": [
                {"role": "system", "content": system_msg},
                {"role": "user", "content": user_msg},
            ],
            "temperature": 0.3,
            "max_tokens": 3500,
        }
        
        print("🌐 Calling Perplexity API...")
        response = requests.post(
            "https://api.perplexity.ai/chat/completions",
            headers=headers,
            json=payload,
            timeout=30
        )
        response.raise_for_status()
        
        result = response.json()
        print("✅ Success! Response received from Perplexity")
        return result['choices'][0]['message']['content']
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}")
        print(f"Response: {e.response.text}")
        return f"❌ Perplexity API HTTP Error: {e.response.text}"
    except Exception as e:
        print(f"Error type: {type(e).__name__}")
        print(f"Error details: {str(e)}")
        return f"❌ Perplexity API failed: {e}"


# Test with sample data
if __name__ == "__main__":
    print("Testing Perplexity AI Weather Overview Integration\n" + "="*60)
    
    # Sample location
    location = {
        'city': 'New York',
        'region': 'New York',
        'country': 'United States'
    }
    
    # Sample hourly data (simplified)
    from datetime import datetime, timedelta
    now = datetime.now()
    hourly_slice = []
    for i in range(48):
        hour_time = now + timedelta(hours=i)
        hourly_slice.append({
            'time': hour_time.isoformat(),
            'temp_f': 45 + (i % 24) / 2,  # Simulated temperature variation
            'precip_prob': min(i * 2, 60),  # Increasing precip probability
            'precip_mm': 0.5 if i > 12 else 0
        })
    
    print(f"\n📍 Location: {location['city']}, {location['region']}")
    print(f"📊 Hourly data points: {len(hourly_slice)}")
    print(f"\n{'='*60}\n")
    
    # Generate forecast
    forecast = generate_ai_overview(location, hourly_slice)
    
    print("\n" + "="*60)
    print("🌐 WEB-BASED AI WEATHER OVERVIEW (Perplexity)")
    print("="*60 + "\n")
    print(forecast)
    print("\n" + "="*60)
