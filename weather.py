import json
import requests


CITIES = [
    "Attock",
    "Bahawalnagar",
    "Bahawalpur",
    "Bhakkar",
    "Chakwal",
    "Chiniot",
    "Faisalabad",
    "Gujranwala",
    "Gujrat",
    "Hafizabad",
    "Jhang",
    "Jhelum",
    "Kasur",
    "Khanewal",
    "Khushab",
    "Lahore",
    "Layyah",
    "Lodhran",
    "Mandi Bahauddin",
    "Multan",
]


def get_weather(c):
    identifier = "f331581e1725a93c28647659d1afcc02"

    api = "http://api.openweathermap.org/data/2.5/weather"
    response = requests.get(url=api, params=dict(q=c, APPID=identifier))
    return response


def fetch_weather(cities):
    dictionary = {}

    print("Fetching results...")
    for city in cities:
        result = get_weather(city)
        obj = json.loads(result.text)
        dictionary[obj["name"]] = obj
    return dictionary


def sort_by_temperature(dictionary):
    cities=[]
    for city_name in sorted(dictionary, key=lambda name: dictionary[name]["main"]["temp"]):
        cities.append((city_name,dictionary[city_name]["main"]["temp"]))
    return cities


def kelvin_to_centi(temp):
    return temp-273


def print_cities(SORTED_CITIES_LIST):
    for name, temperature in SORTED_CITIES_LIST:
        print(name, end="\t")
        print(kelvin_to_centi(temperature))


dictionary = fetch_weather(CITIES)
SORTED_CITIES_LIST = sort_by_temperature(dictionary)
print_cities(SORTED_CITIES_LIST)
