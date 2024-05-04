import requests
from requests.exceptions import HTTPError


def get_weather(city):
    api_key = "f04eac3d3f871e7f61292f0a139352ef"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather = {
            "description": data["weather"][0]["main"],
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"],
            "timezone": data["timezone"],
            "feelslike": data["main"]["feels_like"],
        }
        return weather
    else:
        print("Error fetching weather data:", response.status_code)
        return None


city = "Istanbul"
weather_info = get_weather(city)
if weather_info:
    print(f"Hava {city} şehri için:")
    print("Durum", weather_info["description"])
    print("Sıcaklık:", weather_info["temperature"], "°C")
    print("Hissedilen Sıcaklık:", weather_info["feelslike"], "°C")
    print("Nem:", weather_info["humidity"], "%")
    print("Rüzgar Hızı:", weather_info["wind_speed"], "m/s")


# weather_info = {"description": "thunderstorm with light rain"}
# if weather_info["description"] in [ "thunderstorm with light rain,thunderstorm with rain,thunderstorm with heavy rain,light thunderstorm,thunderstorm,heavy thunderstorm,ragged thunderstorm,thunderstorm with light drizzle,thunderstorm with drizzle,thunderstorm with heavy drizzle"]:
#    print("Durum,thunderstorm")
#
# weather_info = {"description": "clear sky"}
#
# if weather_info["description"] in ["clear sky"]:
#    print("Durum güneşli")
