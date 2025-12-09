# 🚀 Deploy Your Weather App to Streamlit Cloud

## Quick Start Guide

Follow these steps to deploy your weather app to Streamlit Cloud and share it with the world!

---

## 📋 Prerequisites

✅ GitHub account (free)
✅ Streamlit Cloud account (free - sign up with GitHub)
✅ Your weather app code (you already have this!)

---

## Step 1: Push to GitHub

### Option A: Using GitHub Desktop (Easiest)

1. **Download GitHub Desktop** (if not installed)
   - Visit: https://desktop.github.com/
   - Install and sign in with your GitHub account

2. **Create a New Repository**
   - In GitHub Desktop: File → Add Local Repository
   - Browse to: `C:\Users\mtobin\Weather App`
   - Click "Create a repository" if prompted
   - Name: `weather-app`
   - Description: "Real-time weather app with animated radar and multiple weather models"
   - Keep it **Public** (required for free Streamlit Cloud)
   - Click "Create Repository"

3. **Initial Commit**
   - You'll see all your files in the "Changes" tab
   - Summary: "Initial commit - Weather app with radar"
   - Click "Commit to main"

4. **Publish to GitHub**
   - Click "Publish repository" button
   - Uncheck "Keep this code private" (Streamlit Cloud requires public repos for free tier)
   - Click "Publish Repository"

✅ **Done!** Your code is now on GitHub!

---

### Option B: Using Git Command Line

If you prefer command line, run these commands in PowerShell:

```powershell
# Navigate to your project
cd "C:\Users\mtobin\Weather App"

# Initialize git repository
git init

# Add all files
git add .

# Create initial commit
git commit -m "Initial commit - Weather app with animated radar"

# Create repository on GitHub first, then:
# (Replace 'yourusername' with your actual GitHub username)
git branch -M main
git remote add origin https://github.com/yourusername/weather-app.git
git push -u origin main
```

---

## Step 2: Deploy to Streamlit Cloud

1. **Visit Streamlit Cloud**
   - Go to: https://share.streamlit.io
   - Click "Sign in" → Sign in with GitHub
   - Authorize Streamlit to access your GitHub

2. **Create New App**
   - Click "New app" button (top right)
   - **Repository:** Select `yourusername/weather-app`
   - **Branch:** `main`
   - **Main file path:** `weather_streamlit_app.py`
   - **App URL:** (optional) customize your URL
   
3. **Deploy!**
   - Click "Deploy"
   - Wait 2-3 minutes for initial deployment
   - Your app will be live at: `https://yourusername-weather-app.streamlit.app`

✅ **Your app is now live and shareable!**

---

## Step 3: Share Your App

Your app URL will be something like:
```
https://your-github-username-weather-app.streamlit.app
```

Share this URL with anyone - no login required for viewers!

---

## 🔄 Updating Your App

After deployment, any changes you push to GitHub will automatically update your app:

### Using GitHub Desktop:
1. Make changes to your code
2. Open GitHub Desktop
3. Enter commit message
4. Click "Commit to main"
5. Click "Push origin"
6. Wait ~1 minute - your app updates automatically!

### Using Git Command Line:
```bash
git add .
git commit -m "Description of changes"
git push
```

---

## 🎯 What Gets Deployed

Your Streamlit Cloud deployment includes:
- ✅ `weather_streamlit_app.py` - Main app
- ✅ `requirements.txt` - Python dependencies
- ✅ All weather features:
  - 🌐 Multiple weather models (ECMWF, GFS, ICON)
  - 🌧️ Animated radar with RainViewer
  - 📊 Hourly forecasts
  - ⚡ Precipitation alerts
  - 🌡️ Unit conversions

---

## 🛠️ Troubleshooting

### App won't start
- Check that `weather_streamlit_app.py` is the main file
- Verify `requirements.txt` has all dependencies

### Import errors
- Make sure `requirements.txt` is in the root directory
- Check Python version compatibility (app uses Python 3.12 features)

### Slow loading
- First load is always slower (cold start)
- Subsequent loads are faster
- Streamlit Cloud automatically sleeps inactive apps (wakes in ~30 seconds)

---

## 🎨 Customizing Your App

### Update the README
Edit `README.md` and add your live app URL:
```markdown
## 🚀 Live Demo

Visit the live app: https://your-username-weather-app.streamlit.app
```

### Add a Custom Domain (Optional - Paid)
Streamlit Cloud paid plans allow custom domains like `weather.yourdomain.com`

---

## 📊 App Limits (Free Tier)

Streamlit Cloud free tier includes:
- ✅ **Unlimited public apps**
- ✅ **1 GB RAM per app**
- ✅ **1 CPU core**
- ✅ **Community support**
- ⚠️ Apps sleep after inactivity (auto-wake on visit)
- ⚠️ Must be public repos

This is more than enough for your weather app!

---

## 🎉 Success Checklist

- [ ] Code pushed to GitHub
- [ ] Repository is public
- [ ] Signed in to Streamlit Cloud
- [ ] App deployed successfully
- [ ] App URL is accessible
- [ ] Shared URL with friends/colleagues
- [ ] Updated README with live URL

---

## 🔗 Useful Links

- **Streamlit Cloud:** https://share.streamlit.io
- **Documentation:** https://docs.streamlit.io/streamlit-community-cloud
- **GitHub:** https://github.com
- **Support:** https://discuss.streamlit.io

---

## 📞 Need Help?

If you encounter issues:
1. Check Streamlit Cloud logs (click "Manage app" → "Logs")
2. Visit Streamlit Community Forum: https://discuss.streamlit.io
3. Check GitHub repository settings (must be public)

---

**Happy Deploying! 🚀**

Your weather app will be live and accessible to anyone in the world!
