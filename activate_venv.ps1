# Activate Virtual Environment and Run Commands
# Usage: .\activate_venv.ps1

Write-Host "🚀 Activating Virtual Environment..." -ForegroundColor Green

# Activate the virtual environment
& "$PSScriptRoot\venv\Scripts\Activate.ps1"

Write-Host "✅ Virtual Environment Activated!" -ForegroundColor Green
Write-Host ""
Write-Host "📦 Installed Packages:" -ForegroundColor Cyan
pip list
Write-Host ""
Write-Host "💡 Quick Commands:" -ForegroundColor Yellow
Write-Host "   • Run Streamlit App:  python -m streamlit run bus_streamlit_app.py" -ForegroundColor White
Write-Host "   • Run Python Script:  python bus_arequipa.py" -ForegroundColor White
Write-Host "   • Install Package:    pip install <package_name>" -ForegroundColor White
Write-Host "   • Deactivate:         deactivate" -ForegroundColor White
Write-Host ""
