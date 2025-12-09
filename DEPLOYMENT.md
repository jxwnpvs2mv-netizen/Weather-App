# 🚀 Deployment Guide - Streamlit Cloud

## Quick Start - Deploy in 5 Minutes!

### Step 1: Push to GitHub

1. **Initialize Git** (if not already done):
```bash
cd "c:\Users\mtobin\Weather App"
git init
git add .
git commit -m "Initial commit - Weather App"
```

2. **Create GitHub Repository**:
   - Go to [github.com/new](https://github.com/new)
   - Name it: `weather-app` or `streamlit-weather`
   - Keep it Public
   - Don't initialize with README (we already have one)
   - Click "Create repository"

3. **Push to GitHub**:
```bash
git remote add origin https://github.com/YOUR-USERNAME/weather-app.git
git branch -M main
git push -u origin main
```

### Step 2: Deploy to Streamlit Cloud

1. **Go to Streamlit Cloud**:
   - Visit: [share.streamlit.io](https://share.streamlit.io)
   - Click "Sign in with GitHub"
   - Authorize Streamlit

2. **Deploy Your App**:
   - Click "New app" button
   - Select your repository: `YOUR-USERNAME/weather-app`
   - Choose branch: `main`
   - Main file path: `weather_streamlit_app.py`
   - Click "Deploy!"

3. **Wait for Deployment** (usually 2-3 minutes):
   - Streamlit will install dependencies
   - Build and launch your app
   - Provide you with a public URL

### Step 3: Access Your App

Your app will be live at:
```
https://YOUR-USERNAME-weather-app-streamlit.app
```

Or a similar URL provided by Streamlit Cloud.

---

## ✅ Pre-Deployment Checklist

- [x] `requirements.txt` - All dependencies listed
- [x] `.gitignore` - Excludes unnecessary files
- [x] `README.md` - Project documentation
- [x] `.streamlit/config.toml` - App configuration
- [x] `weather_streamlit_app.py` - Main app file

---

## 🔧 Troubleshooting

### Issue: App won't start
**Solution**: Check the logs in Streamlit Cloud dashboard for specific errors

### Issue: Dependencies not installing
**Solution**: Verify `requirements.txt` has correct package names and versions

### Issue: App is slow
**Solution**: Streamlit free tier has 1GB RAM. Optimize code if needed.

---

## 📝 Alternative: Manual GitHub Setup

If you prefer using GitHub Desktop or the web interface:

1. **Create Repository on GitHub.com**:
   - Go to github.com and create new repository
   - Clone it to your computer

2. **Copy Files**:
   - Copy all files from `c:\Users\mtobin\Weather App\` 
   - Into your cloned repository folder
   - Keep these files:
     - `weather_streamlit_app.py`
     - `requirements.txt`
     - `.gitignore`
     - `README.md`
     - `.streamlit/config.toml`

3. **Commit and Push**:
   - Use GitHub Desktop to commit changes
   - Push to GitHub
   - Follow Step 2 above for Streamlit Cloud

---

## 🎨 Customization After Deployment

### Update App Settings:
1. Go to Streamlit Cloud dashboard
2. Click on your app
3. Settings → Advanced settings
4. Modify as needed

### Update Code:
1. Make changes locally
2. Commit and push to GitHub
3. Streamlit Cloud auto-deploys changes!

---

## 🌐 Custom Domain (Optional)

Streamlit Cloud free tier includes:
- Free subdomain: `yourapp.streamlit.app`
- HTTPS/SSL included
- Auto-updates on git push

For custom domain (like `weather.yourdomain.com`):
- Requires Streamlit Cloud Pro plan ($20/month)

---

## 📊 Monitor Your App

After deployment, you can:
- View app logs
- See resource usage
- Monitor visitors
- Restart app if needed

All from the Streamlit Cloud dashboard!

---

## 🚨 Important Notes

1. **Public Repository**: Your code will be public on GitHub
2. **Free Tier Limits**: 
   - 1 GB RAM per app
   - Unlimited apps (but only 1 private app)
   - Community support
3. **Auto-Sleep**: App sleeps after 7 days of inactivity
4. **No Secrets in Code**: Never commit API keys or passwords

---

## 🎉 Success!

Once deployed, share your app with:
- Friends and family
- Social media
- Portfolio
- Resume/LinkedIn

Your weather app is now live and accessible to anyone in the world! 🌍

---

## 📞 Need Help?

- Streamlit Documentation: [docs.streamlit.io](https://docs.streamlit.io)
- Streamlit Community: [discuss.streamlit.io](https://discuss.streamlit.io)
- GitHub Issues: Create issue in your repository
