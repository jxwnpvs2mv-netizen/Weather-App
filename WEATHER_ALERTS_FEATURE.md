# Weather Alerts & Warnings Feature

## Overview
Your Weather App now displays **real-time weather alerts, warnings, and special weather statements** from the National Weather Service (NWS).

## What's Included

### Alert Types Displayed:
- 🚨 **Severe Weather Warnings** (Tornadoes, Severe Thunderstorms, Flash Floods, etc.)
- ⚠️ **Weather Watches** (Tornado Watch, Severe Thunderstorm Watch, etc.)
- ℹ️ **Advisories** (Winter Weather, Wind, Heat, etc.)
- 📢 **Special Weather Statements**
- 🌊 **Marine & Coastal Warnings**
- 🔥 **Fire Weather Warnings**
- ❄️ **Winter Storm Warnings & Advisories**
- 🌪️ **Hurricane & Tropical Storm Warnings**

## Features

### Visual Severity Indicators

**Extreme Severity** (Red):
- 🚨 Background: Dark Red (#8B0000)
- Used for: Tornado Warnings, Flash Flood Emergencies, Extreme Wind Warnings

**Severe** (Orange-Red):
- ⚠️ Background: Orange-Red (#FF4500)
- Used for: Severe Thunderstorm Warnings, Flash Flood Warnings

**Moderate** (Orange):
- ⚠️ Background: Orange (#FFA500)
- Used for: Winter Storm Warnings, Heat Advisories, Wind Advisories

**Minor** (Blue):
- ℹ️ Background: Steel Blue (#4682B4)
- Used for: Special Weather Statements, Frost Advisories

### Alert Information Displayed

**Main Alert Box:**
- 📢 Event name (e.g., "Tornado Warning")
- 📝 Headline summary
- ⏰ Effective time
- ⏱️ Expiration time
- 📍 Affected areas

**Detailed Expandable Section:**
- Full description of the weather threat
- ⚡ What to do (instructions/recommendations)
- Severity level (Extreme, Severe, Moderate, Minor)
- Urgency (Immediate, Expected, Future)
- Certainty (Observed, Likely, Possible)
- Recommended action (Monitor, Execute, Prepare, etc.)
- Issuing office

## How It Works

### Data Source
- **API:** National Weather Service (NWS) API
- **Endpoint:** `https://api.weather.gov/alerts/active`
- **Coverage:** United States and territories only
- **Update Frequency:** Real-time (alerts appear as soon as NWS issues them)

### Integration
1. When you view weather for a US location, the app automatically checks for active alerts
2. Alerts are fetched using the location's latitude/longitude
3. Multiple alerts are sorted by severity (most severe first)
4. Non-US locations gracefully skip alert checking

### Technical Details

**API Parameters:**
- `point`: Coordinates (lat,lon)
- `status`: actual (excludes test/exercise alerts)
- `message_type`: alert,update (current alerts and updates)

**Severity Levels:**
- **Extreme:** Extraordinary threat to life/property
- **Severe:** Significant threat to life/property
- **Moderate:** Possible threat to life/property
- **Minor:** Minimal to no threat to life/property

**Urgency Levels:**
- **Immediate:** Act now
- **Expected:** Within next few hours
- **Future:** In the near future

## Examples

### Tornado Warning
```
🚨 Tornado Warning
A confirmed tornado is on the ground. Take shelter immediately!

⏰ Effective: Dec 9, 2:30 PM
⏱️ Expires: Dec 9, 3:00 PM
📍 Trumbull County, Mahoning County

What To Do:
TAKE COVER NOW! Move to a basement or an interior room 
on the lowest floor of a sturdy building. Avoid windows.
```

### Winter Storm Warning
```
⚠️ Winter Storm Warning
Heavy snow expected. Total snow accumulations of 8 to 12 inches.

⏰ Effective: Dec 9, 6:00 PM
⏱️ Expires: Dec 10, 6:00 AM
📍 Northeast Ohio

What To Do:
If you must travel, keep an extra flashlight, food, and 
water in your vehicle in case of an emergency.
```

### Special Weather Statement
```
ℹ️ Special Weather Statement
Patchy dense fog will continue through mid morning.

⏰ Effective: Dec 9, 5:00 AM
⏱️ Expires: Dec 9, 10:00 AM
📍 Niles, Warren, Youngstown areas

What To Do:
Use low beam headlights and allow extra distance between 
vehicles when driving in fog.
```

## User Experience

### Alert Display Location
Alerts appear **prominently at the top** of the weather display, immediately after the city name, ensuring users see critical warnings first.

### Multiple Alerts
If multiple alerts are active:
- All alerts are displayed
- Sorted by severity (most dangerous first)
- Each alert has its own expandable detail section

### No Alerts
When no alerts are active, the section is hidden entirely (no clutter).

## Benefits

✅ **Safety First:** Critical warnings displayed prominently
✅ **Real-Time:** Updates as NWS issues new alerts
✅ **Comprehensive:** All alert types included
✅ **Visual:** Color-coded severity for quick recognition
✅ **Detailed:** Expandable sections for full information
✅ **User-Friendly:** Clean, easy-to-read format
✅ **Automatic:** No user action required

## Limitations

### Coverage
- ⚠️ **US Only:** NWS API only covers United States and territories
- 🌍 **International:** Non-US locations don't show alerts (graceful fallback)

### Alert Types
- ✅ Includes: Warnings, watches, advisories, statements
- ❌ Excludes: Test alerts, exercise alerts, system messages

### API Reliability
- NWS API is generally reliable but may have occasional outages
- App handles API errors gracefully (fails silently)
- Errors don't affect other weather data display

## Future Enhancements

Possible improvements:
- 🌍 Add international alert sources (Met Office, Environment Canada, etc.)
- 🔔 Browser notifications for new alerts
- 📧 Email/SMS alert subscriptions
- 📊 Alert history and statistics
- 🗺️ Alert polygon overlay on radar map
- 🔊 Audio alert announcements for severe weather
- 📱 Mobile push notifications

## Testing

### Test with Active Alerts:
Search for locations currently under alerts:
- During winter: Search cities with winter storm warnings
- During spring: Search Tornado Alley locations
- During summer: Search locations with heat advisories
- During hurricane season: Search coastal areas

### Test Locations (Examples):
- "Moore, Oklahoma" (tornado-prone)
- "Miami, Florida" (hurricane zone)
- "Buffalo, New York" (winter storms)
- "Phoenix, Arizona" (heat advisories)

## API Documentation

**National Weather Service API:**
- Documentation: https://www.weather.gov/documentation/services-web-api
- Alerts Endpoint: https://api.weather.gov/alerts/active
- Status Page: https://api.weather.gov/
- No API key required
- Free for all users

## Code Changes

**Files Modified:**
- `weather_streamlit_app.py`

**Functions Added:**
1. `get_weather_alerts(latitude, longitude)` - Fetches alerts from NWS API
2. `display_weather_alerts(alerts)` - Displays alerts with styling

**Integration Points:**
- Called in `display_weather()` function
- Positioned after location header, before weather icon
- Only executes for US locations

## Credits

Weather alerts provided by the **National Weather Service (NWS)**, part of the National Oceanic and Atmospheric Administration (NOAA).
