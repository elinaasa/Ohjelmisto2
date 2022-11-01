import json
import requests
hakusana = input("Anna hakusana: ")
pyynto = "https://api.tvmaze.com/search/shows?q=" + hakusana
vastaus = requests.get(pyynto).json()
print