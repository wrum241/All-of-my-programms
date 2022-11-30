import requests

APPID = "9ee737b36fdac46233817522e377256c"  # <-- Put your OpenWeatherMap appid here!
URL_BASE = "https://api.openweathermap.org/data/2.5/"

def current_weather(q: str = "Chicago", appid: str = APPID) -> dict:
    return requests.get(URL_BASE + "weather", params=locals()).json()

if __name__ == "__main__":
    from pprint import pprint

    while True:
        location = input("Enter a location:").strip()
        if location:
            pprint(round((dict.get(current_weather(location), 'main').get('temp')-273), 2))
        else:
            break

