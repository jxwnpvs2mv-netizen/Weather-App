# Fix GitHub Desktop Upload Issue
# This script removes the nested Git repository that's causing upload issues

Write-Host "================================" -ForegroundColor Cyan
Write-Host "   Fix GitHub Desktop Upload    " -ForegroundColor Cyan
Write-Host "================================" -ForegroundColor Cyan
Write-Host ""

$currentPath = Get-Location
Write-Host "Current directory: $currentPath" -ForegroundColor White
Write-Host ""

# Check if nested Weather-App folder exists
$nestedFolder = Join-Path $currentPath "Weather-App"
if (Test-Path $nestedFolder) {
    Write-Host "❌ Found nested 'Weather-App' folder that's causing issues" -ForegroundColor Red
    Write-Host ""
    Write-Host "This folder contains:" -ForegroundColor Yellow
    Get-ChildItem $nestedFolder -Force | ForEach-Object { Write-Host "   - $($_.Name)" -ForegroundColor White }
    Write-Host ""
    
    $remove = Read-Host "Remove this nested folder? This is safe - it's just git metadata (y/n)"
    
    if ($remove -eq "y") {
        Write-Host ""
        Write-Host "Removing nested folder..." -ForegroundColor Cyan
        
        try {
            Remove-Item -Path $nestedFolder -Recurse -Force
            Write-Host "✅ Nested folder removed successfully!" -ForegroundColor Green
        } catch {
            Write-Host "❌ Error removing folder. Try manually deleting 'Weather-App' folder" -ForegroundColor Red
            Write-Host "Error: $_" -ForegroundColor Red
            pause
            exit
        }
    } else {
        Write-Host "Skipping removal..." -ForegroundColor Yellow
        pause
        exit
    }
} else {
    Write-Host "✅ No nested folder found" -ForegroundColor Green
}

Write-Host ""
Write-Host "================================" -ForegroundColor Cyan
Write-Host "   Checking Git Status          " -ForegroundColor Cyan
Write-Host "================================" -ForegroundColor Cyan
Write-Host ""

# Check if this is a git repository
if (Test-Path ".git") {
    Write-Host "✅ This folder is a Git repository" -ForegroundColor Green
    Write-Host ""
    Write-Host "Checking what files Git can see..." -ForegroundColor Cyan
    Write-Host ""
    
    # Show tracked files
    $trackedFiles = git ls-files
    if ($trackedFiles) {
        Write-Host "📁 Tracked files:" -ForegroundColor Green
        $trackedFiles | ForEach-Object { Write-Host "   ✓ $_" -ForegroundColor White }
    } else {
        Write-Host "⚠️  No files are currently tracked" -ForegroundColor Yellow
    }
    
    Write-Host ""
    
    # Show untracked files
    Write-Host "📋 Untracked files:" -ForegroundColor Yellow
    git ls-files --others --exclude-standard | ForEach-Object { Write-Host "   ? $_" -ForegroundColor White }
    
} else {
    Write-Host "⚠️  This is not a Git repository yet" -ForegroundColor Yellow
    Write-Host ""
    $init = Read-Host "Initialize Git repository now? (y/n)"
    
    if ($init -eq "y") {
        git init
        Write-Host "✅ Git repository initialized" -ForegroundColor Green
    }
}

Write-Host ""
Write-Host "================================" -ForegroundColor Cyan
Write-Host "   Next Steps                   " -ForegroundColor Cyan
Write-Host "================================" -ForegroundColor Cyan
Write-Host ""

Write-Host "1. Close GitHub Desktop completely" -ForegroundColor White
Write-Host "2. Reopen GitHub Desktop" -ForegroundColor White
Write-Host "3. File → Add Local Repository" -ForegroundColor White
Write-Host "4. Select this folder: $currentPath" -ForegroundColor White
Write-Host "5. You should now see all your files in the Changes tab" -ForegroundColor White
Write-Host "6. Commit and Publish repository" -ForegroundColor White
Write-Host ""

Write-Host "If you still have issues:" -ForegroundColor Yellow
Write-Host "• Make sure you're adding the correct folder (Weather App, not Weather-App)" -ForegroundColor White
Write-Host "• Check that files aren't in .gitignore" -ForegroundColor White
Write-Host "• Try removing and re-adding the repository in GitHub Desktop" -ForegroundColor White
Write-Host ""

Write-Host "✅ Fix complete!" -ForegroundColor Green
Write-Host ""
pause
