# Toteuta taustapalvelu, joka palauttaa annettua lentokentän ICAO-koodia vastaavan
# lentokentän nimen ja kaupungin JSON-muodossa. Tiedot haetaan opintojaksolla käytetystä
# lentokenttätietokannasta. Esimerkiksi EFHK-koodia vastaava GET-pyyntö annetaan muodossa:
# http://127.0.0.1:5000/kenttä/EFHK. Vastauksen on oltava muodossa:
# {"ICAO":"EFHK", "Name":"Helsinki Vantaa Airport", "Municipality":"Helsinki"}.


import mysql.connector
from flask import Flask, Response
import json

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='Salainensana123',
    autocommit=True
)


def tiedot(ident):
    sql = "SELECT name, municipality FROM airport WHERE ident = '" + ident + "'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return tulos


tiedot = tiedot(input("Kirjoita lentoaseman ICAO-koodi: "))

for t in tiedot:
    print("Lentokenttä", t[0], " sijaitsee kunnassa ", t[1])


app = Flask(__name__)

@app.route(2)
