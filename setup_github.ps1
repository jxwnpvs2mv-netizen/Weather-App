# Git Setup and GitHub Push Script
# Run this script to initialize Git and push to GitHub

Write-Host "🚀 Weather App - Git Setup Script" -ForegroundColor Cyan
Write-Host "=================================" -ForegroundColor Cyan
Write-Host ""

# Check if Git is installed
try {
    $gitVersion = git --version
    Write-Host "✅ Git is installed: $gitVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ Git is not installed!" -ForegroundColor Red
    Write-Host "Please install Git from: https://git-scm.com/download/win" -ForegroundColor Yellow
    exit
}

Write-Host ""
Write-Host "📋 Before we start, make sure you have:" -ForegroundColor Yellow
Write-Host "   1. A GitHub account" -ForegroundColor White
Write-Host "   2. Created a new repository on GitHub" -ForegroundColor White
Write-Host ""

$continue = Read-Host "Ready to continue? (y/n)"
if ($continue -ne "y") {
    Write-Host "Setup cancelled." -ForegroundColor Red
    exit
}

Write-Host ""
Write-Host "🔧 Step 1: Initialize Git Repository" -ForegroundColor Cyan
Write-Host "-------------------------------------" -ForegroundColor Cyan

if (Test-Path ".git") {
    Write-Host "⚠️  Git repository already exists" -ForegroundColor Yellow
    $reinit = Read-Host "Reinitialize? This will keep your history (y/n)"
    if ($reinit -eq "y") {
        git init
        Write-Host "✅ Repository reinitialized" -ForegroundColor Green
    }
} else {
    git init
    Write-Host "✅ Git repository initialized" -ForegroundColor Green
}

Write-Host ""
Write-Host "📝 Step 2: Configure Git User" -ForegroundColor Cyan
Write-Host "------------------------------" -ForegroundColor Cyan

$currentUser = git config user.name
$currentEmail = git config user.email

if ($currentUser) {
    Write-Host "Current user: $currentUser ($currentEmail)" -ForegroundColor White
    $changeUser = Read-Host "Change user? (y/n)"
    if ($changeUser -eq "y") {
        $userName = Read-Host "Enter your name"
        $userEmail = Read-Host "Enter your email"
        git config user.name "$userName"
        git config user.email "$userEmail"
        Write-Host "✅ User updated" -ForegroundColor Green
    }
} else {
    $userName = Read-Host "Enter your name"
    $userEmail = Read-Host "Enter your email"
    git config user.name "$userName"
    git config user.email "$userEmail"
    Write-Host "✅ User configured" -ForegroundColor Green
}

Write-Host ""
Write-Host "📦 Step 3: Add Files to Git" -ForegroundColor Cyan
Write-Host "---------------------------" -ForegroundColor Cyan

Write-Host "Adding files..." -ForegroundColor White
git add .
Write-Host "✅ Files added" -ForegroundColor Green

Write-Host ""
Write-Host "💾 Step 4: Create Initial Commit" -ForegroundColor Cyan
Write-Host "---------------------------------" -ForegroundColor Cyan

git commit -m "Initial commit - Weather App for Streamlit Cloud deployment"
Write-Host "✅ Initial commit created" -ForegroundColor Green

Write-Host ""
Write-Host "🌐 Step 5: Add GitHub Remote" -ForegroundColor Cyan
Write-Host "-----------------------------" -ForegroundColor Cyan
Write-Host ""
Write-Host "Go to GitHub and create a new repository:" -ForegroundColor Yellow
Write-Host "1. Visit: https://github.com/new" -ForegroundColor White
Write-Host "2. Name it: weather-app" -ForegroundColor White
Write-Host "3. Keep it Public" -ForegroundColor White
Write-Host "4. DON'T initialize with README" -ForegroundColor White
Write-Host "5. Click 'Create repository'" -ForegroundColor White
Write-Host ""

$repoUrl = Read-Host "Enter your repository URL (e.g., https://github.com/username/weather-app.git)"

try {
    $existingRemote = git remote get-url origin 2>$null
    if ($existingRemote) {
        Write-Host "⚠️  Remote 'origin' already exists: $existingRemote" -ForegroundColor Yellow
        git remote remove origin
        Write-Host "Removed old remote" -ForegroundColor Yellow
    }
} catch {
    # No existing remote
}

git remote add origin $repoUrl
Write-Host "✅ Remote added" -ForegroundColor Green

Write-Host ""
Write-Host "🚀 Step 6: Push to GitHub" -ForegroundColor Cyan
Write-Host "-------------------------" -ForegroundColor Cyan

git branch -M main
Write-Host "Pushing to GitHub..." -ForegroundColor White
git push -u origin main

if ($LASTEXITCODE -eq 0) {
    Write-Host ""
    Write-Host "🎉 SUCCESS! Your code is now on GitHub!" -ForegroundColor Green
    Write-Host ""
    Write-Host "📋 Next Steps:" -ForegroundColor Cyan
    Write-Host "1. Go to: https://share.streamlit.io" -ForegroundColor White
    Write-Host "2. Sign in with GitHub" -ForegroundColor White
    Write-Host "3. Click 'New app'" -ForegroundColor White
    Write-Host "4. Select your repository" -ForegroundColor White
    Write-Host "5. Choose file: weather_streamlit_app.py" -ForegroundColor White
    Write-Host "6. Click 'Deploy!'" -ForegroundColor White
    Write-Host ""
    Write-Host "Your app will be live in a few minutes! 🌤️" -ForegroundColor Green
} else {
    Write-Host ""
    Write-Host "❌ Push failed!" -ForegroundColor Red
    Write-Host "Common issues:" -ForegroundColor Yellow
    Write-Host "- Check your GitHub credentials" -ForegroundColor White
    Write-Host "- Make sure the repository exists" -ForegroundColor White
    Write-Host "- Verify the repository URL is correct" -ForegroundColor White
}

Write-Host ""
Write-Host "Press any key to exit..."
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
