# Tutustu avoimeen OpenWeather-säärajapintaan: https://openweathermap.org/api.
# Kirjoita ohjelma, joka kysyy käyttäjältä paikkakunnan nimen ja tulostaa sitä vastaavan säätilan tekstin sekä
# lämpötilan Celsius-asteina. Perehdy rajapinnan dokumentaatioon riittävästi. Palveluun rekisteröityminen on tarpeen,
# jotta saat rajapintapyynnöissä tarvittavan API-avaimen (API key). Selvitä myös, miten saat Kelvin-asteet muunnettua
# Celsius-asteiksi.

import requests
CITY = input("Syötä kaupunki: ")
API_KEY = "d0b90774cf56fcc201fcaa1f0cf56da9"
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}"
try:
    vastaus = requests.get(URL)
    if vastaus.status_code == 200:
        json_vastaus = vastaus.json()
        vastaus1 = (json_vastaus["main"]["temp"])
        vastaus2 = (json_vastaus["weather"][2])
        celcius = vastaus1 - 273.15
        print(f"Kaupungin sää: {vastaus2} ja lämpötila {celcius:.1f} °C.")
except requests.exceptions.RequestException as e:
    print("Hakua ei voitu suorittaa.")
