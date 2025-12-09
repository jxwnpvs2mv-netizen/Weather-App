# Virtual Environment Setup and Usage Guide

## ✅ Virtual Environment Created!

Your virtual environment is located at: `c:\Users\mtobin\Weather App\venv\`

## 🚀 How to Use Your Virtual Environment

### Method 1: Using the Helper Script (Recommended)
```powershell
.\activate_venv.ps1
```

### Method 2: Manual Activation
```powershell
.\venv\Scripts\Activate.ps1
```

### Method 3: One-Line Activation + Command
```powershell
.\venv\Scripts\Activate.ps1 ; python bus_arequipa.py
```

## 📦 Installing Packages in Virtual Environment

Once activated, install packages with:
```powershell
pip install streamlit
pip install requests
# or
pip install -r requirements.txt
```

## 🎯 Running Your Apps in the Virtual Environment

### Run the Streamlit Bus App:
```powershell
.\venv\Scripts\Activate.ps1 ; python -m streamlit run bus_streamlit_app.py
```

### Run the Python CLI App:
```powershell
.\venv\Scripts\Activate.ps1 ; python bus_arequipa.py
```

### Run the Weather App:
```powershell
.\venv\Scripts\Activate.ps1 ; python weather.py
```

## 🔄 Deactivating the Virtual Environment

When you're done:
```powershell
deactivate
```

## 📋 Check What's Installed

```powershell
pip list
```

## 🛠️ Useful Commands

### Check Python version in venv:
```powershell
python --version
```

### Check where Python is running from:
```powershell
Get-Command python | Select-Object Source
```

### Reinstall all requirements:
```powershell
pip install --upgrade -r requirements.txt
```

## 📝 Current requirements.txt includes:
- streamlit>=1.28.0
- requests>=2.31.0

## 💡 Tips

1. **Always activate** the venv before running commands to ensure you're using the isolated environment
2. Your prompt will show `(venv)` when the virtual environment is active
3. The venv folder can be deleted and recreated anytime with: `python -m venv venv`
4. Don't commit the `venv` folder to git (it's large and machine-specific)

## 🎉 Quick Start Example

```powershell
# Navigate to your project
cd "c:\Users\mtobin\Weather App"

# Activate virtual environment
.\venv\Scripts\Activate.ps1

# Run your Streamlit app
python -m streamlit run bus_streamlit_app.py

# When done
deactivate
```
