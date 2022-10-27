# Tehtävä on jatkoa aiemmalle autokilpailutehtävälle. Kirjoita Kilpailu-luokka,
# jolla on ominaisuuksina kilpailun nimi, pituus kilometreinä ja osallistuvien autojen lista.
# Luokassa on alustaja, joka saa parametreinaan nimen,
# kilometrimäärän ja autolistan ja asettaa ne ominaisuuksille arvoiksi. Luokassa on seuraavat metodit:
#
# tunti_kuluu, joka toteuttaa aiemmassa autokilpailutehtävässä mainitut tunnin välein tehtävät toimenpiteet
# eli arpoo kunkin auton nopeuden muutoksen ja kutsuu kullekin autolle kulje-metodia.
# tulosta_tilanne, joka tulostaa kaikkien autojen sen hetkiset tiedot selkeäksi taulukoksi muotoiltuna.
# kilpailu_ohi, joka palauttaa True,
# jos jokin autoista on maalissa eli se on ajanut vähintään kilpailun kokonaiskilometrimäärän.
# Kirjoita pääohjelma, joka luo 8000 kilometrin kilpailun nimeltä "Suuri romuralli".
# Luotavalle kilpailulle annetaan kymmenen auton lista samaan tapaan kuin aiemmassa tehtävässä.
# Pääohjelma simuloi kilpailun etenemistä kutsumalla toistorakenteessa aja tunti-metodia,
# jonka jälkeen aina tarkistetaan kilpailu_ohi-metodin avulla, onko kilpailu ohi.
# Ajantasainen tilanne tulostetaan tulosta tilanne-metodin avulla kymmenen tunnin
# välein sekä kertaalleen sen jälkeen, kun kilpailu on päättynyt.
import random


class Auto:
    def __init__(self, rekkari, huippunopeus):
        self.rekkari = rekkari
        self.huippunopeus = huippunopeus
        self.hetknopeus = 0
        self.kuljettumatka = 0

    def kiihdyta(self, nopeudenmuutos):
        self.hetknopeus = self.hetknopeus + nopeudenmuutos
        if self.hetknopeus < 0:
            self.hetknopeus = 0
        elif self.huippunopeus < self.hetknopeus:
            self.hetknopeus = self.huippunopeus

    def kulje(self, tuntimaara):
        self.kuljettumatka = self.kuljettumatka + tuntimaara * self.hetknopeus


class Kilpailu:
    def __init__(self, nimi, pituus_km, osallistuvat_autot):
        self.nimi = nimi
        self.pituus_km = pituus_km
        self.osallistuvat_autot = osallistuvat_autot

    def tunti_kuluu(self):
        for i in self.osallistuvat_autot:
            i.kiihdyta(random.randint(-10, 15))
            i.kulje(1)

    def tulosta_tilanne(self):
        for auto in self.osallistuvat_autot:
            print(
                f"Auton {auto.rekkari} huippunopeus: {auto.huippunopeus} km/h, nykyinen nopeus {auto.hetknopeus} km/h, "
                f"kuljettu matka: {auto.kuljettumatka} km.")

    def kilpailu_ohi(self):
        for i in self.osallistuvat_autot:
            if i.kuljettumatka >= self.pituus_km:
                return True


osallistuvatautot = []
for i in range(10):
    osallistuvatautot.append(Auto("ABC-" + str(i + 1), random.randint(100, 200)))

uusi_kilpailu = Kilpailu("Suuri romuralli", 8000, osallistuvatautot)

kuluneettunnit = 0

while not uusi_kilpailu.kilpailu_ohi():
    uusi_kilpailu.tunti_kuluu()
    kuluneettunnit = kuluneettunnit + 1
    if kuluneettunnit % 10 == 0:
        print(f"\nTunteja kulunut: {kuluneettunnit}")
        uusi_kilpailu.tulosta_tilanne()

print(f"\nKilpailu päättynt. Tunteja kulunut: {kuluneettunnit}")
uusi_kilpailu.tulosta_tilanne()
