# Kirjoita ohjelma, joka hakee ja tulostaa satunnaisen Chuck Norris -vitsin käyttäjälle.
# Käytä seuravalla sivulla esiteltävää rajapintaa: https://api.chucknorris.io/.
# Käyttäjälle on näytettävä pelkkä vitsin teksti.

import requests
pyynto = "https://api.chucknorris.io/jokes/random"
vitsi = requests.get(pyynto)
vitsi_json = vitsi.json()
print(vitsi_json["value"])