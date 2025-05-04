# 🗺️ Restaurant Meeting Logger

A cross-platform Python project for logging restaurant visits, meetings, and automatically visualizing them on a map — complete with Excel export and geolocation.

## 🚀 Features

- 📝 Log restaurant name, visit date, and meeting notes
- 🌍 Automatically finds restaurant address via geolocation
- 📍 Pins restaurant location on an interactive map (`HTML`)
- 📊 Stores meeting data in an Excel file
- 🔁 Opens the map and Excel automatically after saving
- 🧠 If geolocation fails, prompts for manual address entry

---

## 📂 How It Works

1. You run the script.
2. It asks you for:
   - Restaurant name (e.g. `"Sugamour Vilnius"`)
   - Date of visit (e.g. `"2025-04-15"`)
   - Meeting notes (e.g. `"Met with the manager about brunch packages"`)
3. The script:
   - Geolocates the restaurant using the name (and prompts for manual address if needed)
   - Appends the info to `restaurant_meetings.xlsx`
   - Adds a pin to `restaurant_map.html` for that visit
   - Opens both the Excel and the map

---

## 📦 Requirements

Python 3.8 or higher

Install dependencies with pip:

```bash
pip install openpyxl folium geopy
```

---

## 🖥️ Platform Compatibility

✅ Windows  
✅ macOS  
✅ Linux

Platform-specific handling is included to auto-open files after saving.

---

## 🛠️ File Structure

```plaintext
Project_Kornelijus.py        # Main Python script
restaurant_meetings.xlsx     # Auto-generated Excel file (if not already present)
restaurant_map.html          # Interactive map with pins
README.md                    # This file
```

---

## 🔧 To Run the Script

From terminal / command prompt:

```bash
python Project_Kornelijus.py
```

Make sure `restaurant_meetings.xlsx` is **not open** in Excel when running the script, to avoid save errors.

---

## 🧭 Example Input

```plaintext
Restaurant name: Sugamour Vilnius
Date visited: 2025-04-15
Meeting notes: Met with the manager about Easter brunch.
```

---

## 📌 Output

- `restaurant_meetings.xlsx` updated with:
  - Restaurant name
  - Date
  - Full address (auto or manual)
  - Notes
  - Latitude & Longitude
- `restaurant_map.html` updated with a new interactive pin
- Both files opened automatically (if supported by OS)

---

## 🤝 Contributions

Suggestions or pull requests are welcome. Let’s improve this tool together!

---

## 📃 License

MIT License