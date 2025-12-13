"""
Script to remove the corrupted JavaScript section from weather_streamlit_app.py
"""

# Read the file
with open(r"c:\Users\mtobin\Weather App\weather_streamlit_app.py", 'r', encoding='utf-8') as f:
    lines = f.readlines()

print(f"Total lines in file: {len(lines)}")
print(f"\nLine 2081 (index 2080): {repr(lines[2080])}")
print(f"Line 2082 (index 2081): {repr(lines[2081])}")
print(f"Line 2083 (index 2082): {repr(lines[2082])}")

# Find the start of corruption (line with "col1, col2, col3")
corruption_start = None
for i, line in enumerate(lines):
    if i > 2070 and i < 2085 and 'col1, col2, col3 = st.columns(3)' in line:
        corruption_start = i
        print(f"\nFound corruption start at line {i+1}: {repr(line)}")
        break

# Find the end of corruption (line before "def display_weather_alerts")
corruption_end = None
for i, line in enumerate(lines):
    if i > 2100 and 'def display_weather_alerts(alerts):' in line:
        corruption_end = i
        print(f"Found corruption end at line {i+1}: {repr(line)}")
        break

if corruption_start and corruption_end:
    print(f"\nRemoving lines {corruption_start+1} to {corruption_end}")
    print(f"Total lines to remove: {corruption_end - corruption_start}")
    
    # Create new file without corrupted lines
    new_lines = lines[:corruption_start] + ['\n'] + lines[corruption_end:]
    
    # Write back
    with open(r"c:\Users\mtobin\Weather App\weather_streamlit_app.py", 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    
    print(f"\n✅ Fixed! Removed {corruption_end - corruption_start} corrupted lines")
    print(f"New file has {len(new_lines)} lines (was {len(lines)})")
else:
    print("\n❌ Could not locate corruption boundaries")
