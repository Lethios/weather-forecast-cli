import sys
import requests

HELP_MESSAGE = """
Weather CLI Tool

Usage:
    python weather-cli.py <location>

Arguments:
    <location>     The name of the location for which you want the weather report.
                   Examples: "London", "New York", "Tokyo".

Example:
    python weather-cli.py "Tokyo, Japan"
    python weather-cli.py "New York"

Note:
    Ensure that your API key is correctly set in the script.
"""

location = str(sys.argv[1])
if len(sys.argv) < 2:
    print("Error: Please provide a location.")
    print(HELP_MESSAGE)
    sys.exit(1)

elif sys.argv[1] == "help":
    print(HELP_MESSAGE)
    sys.exit(1)

API_KEY = "YOUR_API_KEY"
URL = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}?unitGroup=metric&key={API_KEY}"

try:    
    response = requests.get(URL)
    response.raise_for_status()
    
    data = response.json()
    
    if 'days' not in data or not data['days']:
        raise ValueError(f"No weather data found for {location}")

except requests.exceptions.RequestException as e:
    print(f"Error fetching weather data: {e}")
    sys.exit(1)

except ValueError as e:
    print(f"Error processing the data: {e}")
    sys.exit(1)

except KeyError as e:
    print(f"Error: Missing expected key in the response: {e}")
    sys.exit(1)

except Exception as e:
    print(f"An unexpected error occurred: {e}")
    sys.exit(1)

RESET = "\033[0m"
BOLD = "\033[1m"
RED = "\033[31m"
ORANGE = "\033[38;5;214m"
YELLOW = "\033[33m"
GREEN = "\033[32m"
CYAN = "\033[36m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"

def weather_report():
    day_info = data["days"][0]

    print()
    print(BOLD + CYAN + "Weather Report for " + data['resolvedAddress'] + " (Timezone: " + data['timezone'] + ")" + RESET)

    print(YELLOW + "═" * 55 + RESET)

    print(BOLD + MAGENTA + "Date:       " + RESET + f" {day_info['datetime']}")

    print()
    print(BOLD + RED + "Temperature:" + RESET + f" {day_info['temp']}°C")
    print(BOLD + GREEN + "Condition:  " + RESET + f" {day_info['description']}")

    print()
    print(BOLD + CYAN + "Humidity:   " + RESET + f" {day_info['humidity']}%")
    print(BOLD + CYAN + "Rainfall:   " + RESET + f" {day_info['precip']} mm")

    print()
    print(BOLD + BLUE + "Wind:       " + RESET + f" {day_info['windspeed']} km/h")
    print(BOLD + BLUE + "Pressure:   " + RESET + f" {day_info['pressure']} hPa")

    print()
    print(BOLD + ORANGE + "Sunrise:    " + RESET + f" {day_info['sunrise']}")
    print(BOLD + ORANGE + "Sunset:     " + RESET + f" {day_info['sunset']}")

    print(YELLOW + "═" * 55 + RESET)

    print(BOLD + MAGENTA + "Data Source: " + RESET + " Visual Crossing Weather API")

    print(YELLOW + "═" * 55 + RESET)

weather_report()
