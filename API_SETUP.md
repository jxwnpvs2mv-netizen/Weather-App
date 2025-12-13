# API Keys Setup Guide

## 🔐 Security Notice
All API keys are stored in the `.env` file which is **NOT** committed to GitHub.

## 📝 Setup Instructions

### 1. Create `.env` File
Copy `.env.example` to `.env`:
```powershell
Copy-Item .env.example .env
```

### 2. Add Your API Keys
Open `.env` and replace the placeholders with your actual API keys:

```env
PERPLEXITY_API_KEY=your_actual_perplexity_key_here
VISUAL_CROSSING_API_KEY=your_actual_visual_crossing_key_here
OPENAI_API_KEY=your_actual_openai_key_here
WINDY_API_KEY=your_actual_windy_key_here
```

### 3. Get API Keys

#### Perplexity AI (for AI weather overview)
- Sign up: https://www.perplexity.ai/
- Get API key from dashboard

#### Visual Crossing (for weather data)
- Sign up: https://www.visualcrossing.com/sign-up
- Free tier: 1000 records/day

#### OpenAI (optional - for additional AI features)
- Get key: https://platform.openai.com/api-keys

#### Windy.com (for interactive maps)
- Get key: https://api.windy.com/keys

## 🚀 Deployment

### Streamlit Community Cloud
1. Push your code to GitHub (`.env` will be automatically ignored)
2. Go to https://streamlit.io/cloud
3. Deploy your app
4. Add secrets in Streamlit dashboard:
   ```toml
   PERPLEXITY_API_KEY = "your_key"
   VISUAL_CROSSING_API_KEY = "your_key"
   OPENAI_API_KEY = "your_key"
   WINDY_API_KEY = "your_key"
   ```

### Other Platforms (Heroku, Railway, etc.)
Set environment variables in platform dashboard:
```bash
PERPLEXITY_API_KEY=your_key
VISUAL_CROSSING_API_KEY=your_key
OPENAI_API_KEY=your_key
WINDY_API_KEY=your_key
```

## ✅ Security Checklist
- ✅ `.env` file in `.gitignore`
- ✅ No hardcoded API keys in code
- ✅ `.env.example` contains only placeholders
- ✅ API keys loaded from environment variables
