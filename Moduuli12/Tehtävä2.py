import requests
from api import api as key
"""
kunta = input("Mikä kunta? ")
api2 = requests.get(f"https://api.openweathermap.org/geo/1.0/direct?q={kunta}&appid={key}")
api2 = api2.json()
nimi = api2[0]["name"]
kordinaatit = [api2[0]["lat"], api2[0]["lon"]]
saa = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={kordinaatit[0]}&lon={kordinaatit[1]}&appid={key}")
saa = saa.json()
kuvaus = saa["weather"][0]["description"]
lampotila = f"{saa["main"]["temp"]-273.15:.2f}"
print(f"Kunta: {nimi}\nKuvaus: {kuvaus}\nLämpötila: {lampotila} celsius astetta")
"""

kunta = input("Mikä kunta? ")
haku = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={kunta},fi&appid={key}")
haku = haku.json()
kuvaus = haku["weather"][0]["description"]
lampotila = f"{haku["main"]["temp"]-273.15:.2f}"
print(f"Kunta: {kunta}\nKuvaus: {kuvaus}\nLämpötila: {lampotila} celsius astetta")