# Visual Crossing API Setup Guide

## Overview

The weather app uses **Visual Crossing Weather API** for professional daily weather outlooks with natural language descriptions!

### Features
- 📝 **Natural language descriptions** - Professional weather summaries
- 🆓 **Free tier** - 1000 records/day at no cost
- ⚡ **Fast & reliable** - Professional weather descriptions
- 🔒 **No credit card required** - Sign up with just an email

---

## Quick Start

### 1. Sign Up for Free API Key

1. Visit [Visual Crossing Sign Up](https://www.visualcrossing.com/sign-up)
2. Create a free account (no credit card needed)
3. Copy your API key from the account dashboard

### 2. Add API Key to the App

**Option A: Through the App UI (Recommended)**
1. Open the weather app in your browser
2. Look for the sidebar on the left
3. Find the **"🔑 Visual Crossing API (Optional)"** section
4. Click to expand "Configure API Key for Better Outlook"
5. Paste your API key in the text field
6. Click **"Save API Key"**
7. Done! The app will now use Visual Crossing for daily outlooks

**Option B: Environment Variable**
1. Set an environment variable:
   ```powershell
   # Windows PowerShell
   $env:VISUAL_CROSSING_API_KEY = "your_api_key_here"
   
   # Or add to system environment variables permanently
   ```

2. Restart the app

---

## How It Works

### With Visual Crossing API Key
```
📅 Today's Outlook
Partly cloudy throughout the day with a chance of afternoon thunderstorms.
```

### Without API Key
The daily outlook section will not display until you configure your API key. 
You'll see a helpful message: "💡 Add a Visual Crossing API key in the sidebar for daily weather outlook descriptions. It's free!"

---

## Free Tier Limits

| Feature | Limit |
|---------|-------|
| Records per day | 1,000 |
| API calls | Unlimited (counts by records) |
| Credit card | Not required |
| Cost | $0 |

**What's a record?**
- Each day requested = 1 record
- Each hour = 1 record
- Our app requests **only 1 record per lookup** (today's description only)

**Example:** With 1000 records/day, you can check weather for different locations up to 1000 times per day!

---

## Troubleshooting

### "Invalid API key" Warning
- Check that you copied the full API key correctly
- Make sure there are no extra spaces
- Verify your account is active at visualcrossing.com

### Not Seeing Daily Outlook
- Make sure you clicked "Save API Key" after entering it
- Check that the API key was copied completely (no extra spaces)
- Verify you're signed in at visualcrossing.com
- Check if you exceeded your daily limit (1000 records)

### API Key Not Working
If Visual Crossing API is unavailable:
- Check your internet connection
- Verify the API key is correct
- Make sure you haven't exceeded the free tier limit
- Try generating a new API key from your dashboard

---

## API Documentation

For more details about Visual Crossing API:
- [Timeline Weather API Docs](https://www.visualcrossing.com/resources/documentation/weather-api/timeline-weather-api/)
- [API Query Builder](https://www.visualcrossing.com/weather-query-builder/)

---

## Privacy & Security

- API keys are stored only in your browser session
- Keys are not saved to disk or shared
- Keys are not visible in the UI (password field)
- You can clear the key anytime by clicking "Clear API Key"

---

## Why Visual Crossing?

| Feature | Details |
|---------|---------|
| **Style** | Professional, natural language descriptions |
| **Detail** | Rich, detailed weather narratives |
| **Cost** | Free tier: 1000 records/day |
| **Reliability** | 99.9% uptime guarantee |
| **Setup** | Simple one-time API key configuration |

---

## Example Descriptions

Visual Crossing provides natural, professional weather descriptions:

- "Partly cloudy throughout the day."
- "Becoming cloudy in the afternoon."
- "Clear conditions throughout the day."
- "Cloudy skies with a chance of rain in the evening."
- "Partly cloudy with morning rain."
- "Clear conditions with a chance of afternoon thunderstorms."

---

## Support

Need help?
- Check the [Visual Crossing Support](https://www.visualcrossing.com/support/)
- Visit their [Community Forums](https://support.visualcrossing.com/hc/en-us/community/topics)

Enjoy enhanced weather outlooks! 🌤️
