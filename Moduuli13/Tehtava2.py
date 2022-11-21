# Toteuta taustapalvelu, joka palauttaa annettua lentokentän ICAO-koodia vastaavan
# lentokentän nimen ja kaupungin JSON-muodossa. Tiedot haetaan opintojaksolla käytetystä
# lentokenttätietokannasta. Esimerkiksi EFHK-koodia vastaava GET-pyyntö annetaan muodossa:
# http://127.0.0.1:5000/kenttä/EFHK. Vastauksen on oltava muodossa:
# {"ICAO":"EFHK", "Name":"Helsinki Vantaa Airport", "Municipality":"Helsinki"}.


import mysql.connector
from flask import Flask, Response

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='Salainensana123',
    autocommit=True
)

app = Flask(__name__)


@app.route('/kentta/<ident>')
def tiedot(ident):
    sql = "SELECT ident, name, municipality FROM airport WHERE ident = '" + ident + "'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchone()
    print(tulos)

    json = {
        "ICAO": tulos[0],
        "Name": tulos[2],
        "Municipality": tulos[1]
    }
    return json


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
