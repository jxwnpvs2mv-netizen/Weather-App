# 🔧 GitHub Desktop Not Uploading Files - FIX

## Problem
GitHub Desktop isn't showing your files or uploading your folder contents.

## Cause
There's a **nested Git repository** (`Weather-App/` folder inside your main folder) that's confusing GitHub Desktop.

---

## ✅ Quick Fix (Choose One)

### Option 1: Run the Fix Script (Easiest)

1. Right-click `fix_github_upload.ps1`
2. Select "Run with PowerShell"
3. Follow the prompts
4. Close and reopen GitHub Desktop
5. Re-add the repository

---

### Option 2: Manual Fix

#### Step 1: Remove Nested Folder
```powershell
# Open PowerShell in your project folder
cd "C:\Users\mtobin\Weather App"

# Remove the nested folder
Remove-Item -Path "Weather-App" -Recurse -Force
```

#### Step 2: Restart GitHub Desktop
1. Close GitHub Desktop completely
2. Reopen GitHub Desktop

#### Step 3: Re-add Repository
1. File → Remove repository (if it's there)
2. File → Add Local Repository
3. Browse to: `C:\Users\mtobin\Weather App` (NOT Weather-App!)
4. Click "Add Repository"

---

## 🎯 Verify It's Working

After the fix, you should see these files in GitHub Desktop:

✅ Files that SHOULD appear:
- `weather_streamlit_app.py` ⭐ (main app)
- `weather.py`
- `requirements.txt`
- `README.md`
- `.gitignore`
- `.streamlit/` folder
- `DEPLOYMENT.md`
- `LICENSE`
- And other documentation files

❌ Files that should NOT appear (correctly ignored):
- `venv/` folder
- `__pycache__/`
- `.env` files

---

## 🔍 Common Issues

### Issue 1: "Repository already exists"
**Solution:**
1. In GitHub Desktop: Repository → Remove
2. File → Add Local Repository
3. Select the correct folder

### Issue 2: "Not a Git repository"
**Solution:**
```powershell
cd "C:\Users\mtobin\Weather App"
git init
```
Then re-add in GitHub Desktop

### Issue 3: Files still not showing
**Solution:**
Check if files are in `.gitignore`:
```powershell
# See what Git can see
git status

# See what's ignored
git status --ignored
```

### Issue 4: Wrong folder added
**Make sure you're adding:**
```
✅ C:\Users\mtobin\Weather App
```
**NOT:**
```
❌ C:\Users\mtobin\Weather App\Weather-App
```

---

## 📋 Step-by-Step: Fresh Start

If you want to start completely fresh:

```powershell
# 1. Navigate to parent folder
cd C:\Users\mtobin

# 2. Rename current folder
Rename-Item "Weather App" "Weather App OLD"

# 3. Create new folder
New-Item -ItemType Directory -Path "Weather-App-Deploy"
cd "Weather-App-Deploy"

# 4. Copy only the files you need (not venv!)
Copy-Item "C:\Users\mtobin\Weather App OLD\weather_streamlit_app.py" .
Copy-Item "C:\Users\mtobin\Weather App OLD\weather.py" .
Copy-Item "C:\Users\mtobin\Weather App OLD\requirements.txt" .
Copy-Item "C:\Users\mtobin\Weather App OLD\README.md" .
Copy-Item "C:\Users\mtobin\Weather App OLD\.gitignore" .
Copy-Item "C:\Users\mtobin\Weather App OLD\.streamlit" . -Recurse

# 5. Initialize Git
git init
git add .
git commit -m "Initial commit"

# 6. Add in GitHub Desktop
```

---

## ✅ Checklist

After fix, verify:
- [ ] Nested `Weather-App/` folder is deleted
- [ ] GitHub Desktop shows all your files
- [ ] You can see `weather_streamlit_app.py` in Changes
- [ ] Commit message box is editable
- [ ] "Publish repository" button is clickable

---

## 🆘 Still Having Issues?

### Check Git Status
```powershell
cd "C:\Users\mtobin\Weather App"
git status
```

Should show your files, not say "nothing to commit"

### Verify Repository
```powershell
# Should show "main" or "master"
git branch

# Should list your files
git ls-files
```

### Reset Everything
```powershell
# Nuclear option - start fresh
cd "C:\Users\mtobin\Weather App"
Remove-Item .git -Recurse -Force
git init
git add .
git commit -m "Initial commit"
```

---

## 📞 Need More Help?

If still not working:
1. Take a screenshot of GitHub Desktop showing the issue
2. Run: `git status` and save the output
3. Check: What folder is shown in GitHub Desktop's title bar?
4. Is it the right folder?

The issue is almost always:
- ✅ Wrong folder selected
- ✅ Nested git repository
- ✅ Files in .gitignore

---

**Run `fix_github_upload.ps1` to automatically fix the nested repository issue!**
