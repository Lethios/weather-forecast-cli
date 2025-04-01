# Weather Forecast CLI

Weather Forecast CLI is a simple command-line tool to fetch and display weather data for any location using the Visual Crossing Weather API.


## Features
- Real-time weather reports (temperature, humidity, wind speed, etc.).
- Colorful terminal output for better readability.
- Simple usage—just provide a location name.
- Error handling for invalid inputs or API failures.


## Installation
1. **Ensure Python is installed (Python 3.x recommended).**
2. **Install the required dependency:**
   ```bash
   pip install requests


## Usage
Run the program using Python:
```bash
python weather-cli.py "LOCATION"
```
**Examples:**
```bash
python weather-cli.py "Tokyo, Japan"
python weather-cli.py "New York"
```


## Configuration:
1. Replace `YOUR_API_KEY` in the script with your [Visual Crossing API](https://www.visualcrossing.com/weather-api) key.
2. (Optional) Customize colors in the script by modifying the ANSI escape codes (e.g., `RED = "\033[31m"`).


## Author
**Lethios**
- Github: [@Lethios](https://github.com/Lethios)
- Twitter: [@LethiosDev](https://x.com/LethiosDev)


## License
Copyright © 2025 [Lethios](https://github.com/Lethios).  
This project is licensed under the [MIT License](LICENSE).
